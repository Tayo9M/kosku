"""
API endpoints for realtime data validation
"""

import json
import calendar
from datetime import datetime, date

from flask import jsonify, request
from flask_login import login_required

from app import app, db
from models import Property, Room, OccupancyRecord, FinancialRecord
from auth_helpers import get_user_properties

@app.route('/api/room_stats_data', methods=['GET'])
@login_required
def api_room_stats_data():
    """API endpoint to get room statistics data"""
    property_id = request.args.get('property_id', None)
    month = request.args.get('month', datetime.now().strftime('%Y-%m'))
    
    # Get accessible properties for current user
    accessible_properties = get_user_properties()
    
    if not accessible_properties:
        return jsonify({'error': 'No accessible properties'}), 400
        
    if property_id is None:
        property_id = accessible_properties[0].id
    else:
        property_id = int(property_id)
    
    # Check if property is accessible
    property_found = False
    for prop in accessible_properties:
        if prop.id == property_id:
            property_found = True
            property_obj = prop
            break
    
    if not property_found:
        return jsonify({'error': 'Property not accessible'}), 403
    
    # Get rooms for this property
    rooms = Room.query.filter_by(property_id=property_id).all()
    
    # Count rooms by type and status
    room_stats = {}
    for r in rooms:
        if r.room_type not in room_stats:
            room_stats[r.room_type] = {'total': 0, 'occupied': 0, 'available': 0}
        
        room_stats[r.room_type]['total'] += 1
        
        # Check if room is occupied
        occupied = OccupancyRecord.query.filter(
            OccupancyRecord.room_id == r.id,
            OccupancyRecord.month == month,
            OccupancyRecord.is_occupied == True
        ).first() is not None
        
        if occupied:
            room_stats[r.room_type]['occupied'] += 1
        else:
            room_stats[r.room_type]['available'] += 1
    
    # Calculate totals
    total_rooms = sum(stats['total'] for stats in room_stats.values())
    total_occupied = sum(stats['occupied'] for stats in room_stats.values())
    total_available = sum(stats['available'] for stats in room_stats.values())
    occupancy_rate = (total_occupied / total_rooms * 100) if total_rooms > 0 else 0
    
    # Prepare data for charts
    room_types = list(room_stats.keys())
    total_values = [int(stats['total']) for stats in room_stats.values()]
    occupied_values = [int(stats['occupied']) for stats in room_stats.values()]
    available_values = [int(stats['available']) for stats in room_stats.values()]
    
    # Prepare data for response
    response_data = {
        'property_name': property_obj.name,
        'month': month,
        'total_rooms': total_rooms,
        'total_occupied': total_occupied,
        'total_available': total_available,
        'occupancy_rate': round(occupancy_rate, 2),
        'room_stats': room_stats,
        'chart_data': {
            'room_types': room_types,
            'total_values': total_values,
            'occupied_values': occupied_values,
            'available_values': available_values
        }
    }
    
    return jsonify(response_data)

@app.route('/api/financial_stats_data', methods=['GET'])
@login_required
def api_financial_stats_data():
    """API endpoint to get financial statistics data"""
    property_id = request.args.get('property_id', None)
    year = request.args.get('year', str(datetime.now().year))
    
    # Get accessible properties for current user
    accessible_properties = get_user_properties()
    
    if not accessible_properties:
        return jsonify({'error': 'No accessible properties'}), 400
        
    if property_id is None:
        property_id = accessible_properties[0].id
    else:
        property_id = int(property_id)
    
    # Check if property is accessible
    property_found = False
    for prop in accessible_properties:
        if prop.id == property_id:
            property_found = True
            property_obj = prop
            break
    
    if not property_found:
        return jsonify({'error': 'Property not accessible'}), 403
    
    # Prepare data for each month
    months = [calendar.month_name[i] for i in range(1, 13)]
    income_values = []
    expense_values = []
    
    for i in range(1, 13):
        start_date = date(int(year), i, 1)
        if i == 12:
            end_date = date(int(year) + 1, 1, 1)
        else:
            end_date = date(int(year), i + 1, 1)
        
        # Query income and expense
        income = db.session.query(db.func.sum(FinancialRecord.amount)).filter(
            FinancialRecord.transaction_type == 'income',
            FinancialRecord.transaction_date >= start_date,
            FinancialRecord.transaction_date < end_date,
            FinancialRecord.property_id == property_id
        ).scalar() or 0
        
        expense = db.session.query(db.func.sum(FinancialRecord.amount)).filter(
            FinancialRecord.transaction_type == 'expense',
            FinancialRecord.transaction_date >= start_date,
            FinancialRecord.transaction_date < end_date,
            FinancialRecord.property_id == property_id
        ).scalar() or 0
        
        # Convert Decimal to float for JSON serialization
        income_values.append(float(income) if hasattr(income, 'real') else income)
        expense_values.append(float(expense) if hasattr(expense, 'real') else expense)
    
    # Calculate profit by month
    profit_values = [income_values[i] - expense_values[i] for i in range(len(income_values))]
    
    # Generate colors for profit chart
    profit_colors = []
    for profit in profit_values:
        if profit >= 0:
            profit_colors.append('rgba(75, 192, 192, 0.5)')
        else:
            profit_colors.append('rgba(255, 99, 132, 0.5)')
    
    # Calculate yearly totals
    yearly_income = sum(income_values)
    yearly_expense = sum(expense_values)
    yearly_profit = yearly_income - yearly_expense
    
    # Prepare monthly data
    monthly_data = []
    for i in range(12):
        monthly_data.append({
            'month': months[i],
            'income': income_values[i],
            'expense': expense_values[i],
            'profit': profit_values[i]
        })
    
    # Prepare data for response
    response_data = {
        'property_name': property_obj.name,
        'year': year,
        'yearly_income': yearly_income,
        'yearly_expense': yearly_expense,
        'yearly_profit': yearly_profit,
        'monthly_data': monthly_data,
        'chart_data': {
            'months': months,
            'income_values': income_values,
            'expense_values': expense_values,
            'profit_values': profit_values,
            'profit_colors': profit_colors
        }
    }
    
    return jsonify(response_data)