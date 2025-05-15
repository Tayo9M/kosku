"""
File ini berisi fungsi-fungsi yang dimodifikasi untuk menggunakan Chart.js.
Gunakan file ini untuk mengganti fungsi di routes.py.
"""

import json
import calendar
from datetime import datetime, date

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required

from app import app, db
from models import Property, Room, OccupancyRecord, FinancialRecord
from auth_helpers import get_user_properties

@app.route('/room_stats')
@login_required
def room_stats():
    # Get property ID from request or default to first accessible property
    property_id = request.args.get('property_id', None)
    month = request.args.get('month', datetime.now().strftime('%Y-%m'))
    
    # Get accessible properties for current user
    accessible_properties = get_user_properties()
    
    if not accessible_properties:
        flash('Anda tidak memiliki akses ke properti manapun', 'danger')
        return redirect(url_for('reports'))
        
    if property_id is None:
        property_id = accessible_properties[0].id
    else:
        property_id = int(property_id)
    
    # Get property details
    property_obj = Property.query.get_or_404(property_id)
    
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
    
    # Prepare data for charts - ensure they're all int/float for JSON serialization
    room_types = list(room_stats.keys())
    total_values = [int(stats['total']) for stats in room_stats.values()]
    occupied_values = [int(stats['occupied']) for stats in room_stats.values()]
    available_values = [int(stats['available']) for stats in room_stats.values()]
    
    return render_template(
        'room_stats_js.html',
        property=property_obj,
        month=month,
        rooms=rooms,
        room_stats=room_stats,
        properties=accessible_properties,
        total_rooms=total_rooms,
        total_occupied=total_occupied,
        total_available=total_available,
        occupancy_rate=occupancy_rate,
        room_types=json.dumps(room_types),
        total_values=json.dumps(total_values),
        occupied_values=json.dumps(occupied_values),
        available_values=json.dumps(available_values)
    )

@app.route('/financial_stats')
@login_required
def financial_stats():
    # Get property ID and year from request
    property_id = request.args.get('property_id', None)
    year = request.args.get('year', str(datetime.now().year))
    
    # Get accessible properties for current user
    accessible_properties = get_user_properties()
    
    if not accessible_properties:
        flash('Anda tidak memiliki akses ke properti manapun', 'danger')
        return redirect(url_for('reports'))
        
    if property_id is None:
        property_id = accessible_properties[0].id
    else:
        property_id = int(property_id)
    
    # Get property details
    property_obj = Property.query.get_or_404(property_id)
    
    # Prepare data for each month
    months = [calendar.month_name[i] for i in range(1, 13)]
    income_values_raw = []
    expense_values_raw = []
    
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
        income_values_raw.append(float(income) if hasattr(income, 'real') else income)
        expense_values_raw.append(float(expense) if hasattr(expense, 'real') else expense)
    
    # Calculate profit by month (convert to float first)
    profit_values_raw = [income_values_raw[i] - expense_values_raw[i] for i in range(len(income_values_raw))]
    
    # Generate colors for profit chart
    profit_colors = []
    for profit in profit_values_raw:
        if profit >= 0:
            profit_colors.append('rgba(75, 192, 192, 0.5)')
        else:
            profit_colors.append('rgba(255, 99, 132, 0.5)')
    
    # Calculate yearly totals (using raw values before JSON conversion)
    yearly_income = sum(income_values_raw)
    yearly_expense = sum(expense_values_raw)
    yearly_profit = yearly_income - yearly_expense
    
    # Prepare monthly data (using raw values)
    monthly_data = []
    for i in range(12):
        monthly_data.append({
            'month': months[i],
            'income': income_values_raw[i],
            'expense': expense_values_raw[i],
            'profit': profit_values_raw[i]
        })
    
    # Get years for dropdown
    current_year = datetime.now().year
    years = list(range(current_year - 2, current_year + 1))
    
    return render_template(
        'financial_stats_js.html',
        property=property_obj,
        year=year,
        yearly_income=yearly_income,
        yearly_expense=yearly_expense,
        yearly_profit=yearly_profit,
        properties=accessible_properties,
        years=years,
        monthly_data=monthly_data,
        months=json.dumps(months),
        income_values=json.dumps(income_values_raw),
        expense_values=json.dumps(expense_values_raw),
        profit_values=json.dumps(profit_values_raw),
        profit_colors=json.dumps(profit_colors)
    )