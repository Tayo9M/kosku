"""
API and routes for animated occupancy rate heat map
"""

import json
import calendar
from datetime import datetime, date, timedelta

from flask import render_template, request, jsonify
from flask_login import login_required, current_user

from app import app, db
from models import Property, Room, OccupancyRecord
from auth_helpers import get_user_properties
from decimal import Decimal

# Custom JSON encoder for Decimal objects
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

@app.route('/heatmap')
@login_required
def occupancy_heatmap():
    """Render the occupancy heat map page"""
    accessible_properties = get_user_properties()
    
    # Default to last 6 months if not specified
    end_date = datetime.now().date().replace(day=1)
    start_date = (end_date - timedelta(days=180)).replace(day=1)
    
    # Get all months between start and end date
    months = []
    current_date = start_date
    while current_date <= end_date:
        months.append(current_date.strftime('%Y-%m'))
        # Move to next month
        if current_date.month == 12:
            current_date = current_date.replace(year=current_date.year + 1, month=1)
        else:
            current_date = current_date.replace(month=current_date.month + 1)
    
    return render_template(
        'occupancy_heatmap.html',
        properties=accessible_properties,
        months=months,
        start_month=start_date.strftime('%Y-%m'),
        end_month=end_date.strftime('%Y-%m')
    )

@app.route('/api/heatmap_data')
@login_required
def api_heatmap_data():
    """API endpoint to get occupancy data for heat map"""
    # Get date range parameters
    start_month = request.args.get('start_month', None)
    end_month = request.args.get('end_month', None)
    
    if not start_month or not end_month:
        # Default to last 6 months if not specified
        end_date = datetime.now().date().replace(day=1)
        start_date = (end_date - timedelta(days=180)).replace(day=1)
        start_month = start_date.strftime('%Y-%m')
        end_month = end_date.strftime('%Y-%m')
    
    # Get all months between start and end month
    start_year, start_month_num = map(int, start_month.split('-'))
    end_year, end_month_num = map(int, end_month.split('-'))
    
    months = []
    current_year, current_month = start_year, start_month_num
    
    while (current_year < end_year) or (current_year == end_year and current_month <= end_month_num):
        months.append(f"{current_year}-{current_month:02d}")
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
    
    # Get accessible properties
    accessible_properties = get_user_properties()
    property_names = [prop.name for prop in accessible_properties]
    property_ids = [prop.id for prop in accessible_properties]
    
    # Initialize data structure for heatmap
    heatmap_data = []
    
    # Get occupancy data for each property and month
    for property_id, property_name in zip(property_ids, property_names):
        property_data = {"property": property_name, "months": []}
        
        for month in months:
            # Count total rooms for this property
            total_rooms = Room.query.filter_by(property_id=property_id).count()
            
            if total_rooms == 0:
                occupancy_rate = 0
            else:
                # Count occupied rooms for this month
                occupied_rooms = db.session.query(db.func.count(OccupancyRecord.id)).filter(
                    OccupancyRecord.month == month,
                    OccupancyRecord.is_occupied == True,
                    OccupancyRecord.room_id.in_(
                        db.session.query(Room.id).filter(Room.property_id == property_id)
                    )
                ).scalar() or 0
                
                # Calculate occupancy rate
                occupancy_rate = (occupied_rooms / total_rooms) * 100
            
            # Add to property data
            property_data["months"].append({
                "month": month,
                "rate": round(occupancy_rate, 1)
            })
        
        heatmap_data.append(property_data)
    
    # Prepare months labels for display (convert YYYY-MM to Month YYYY)
    month_labels = []
    for month in months:
        year, month_num = map(int, month.split('-'))
        month_name = calendar.month_name[month_num]
        month_labels.append(f"{month_name[:3]} {year}")
    
    response_data = {
        "properties": property_names,
        "months": months,
        "month_labels": month_labels,
        "data": heatmap_data
    }
    
    return jsonify(response_data)

@app.route('/api/property_occupancy_trend')
@login_required
def api_property_occupancy_trend():
    """API endpoint to get occupancy trend data for a specific property"""
    property_id = request.args.get('property_id', None)
    months = request.args.get('months', 12)  # Default to 12 months
    
    try:
        months = int(months)
    except ValueError:
        months = 12
    
    if not property_id:
        return jsonify({'error': 'Property ID is required'}), 400
    
    # Verify property access
    accessible_properties = get_user_properties()
    property_found = False
    property_obj = None
    
    for prop in accessible_properties:
        if str(prop.id) == str(property_id):
            property_found = True
            property_obj = prop
            break
    
    if not property_found or property_obj is None:
        return jsonify({'error': 'Property not accessible'}), 403
    
    # Generate months list (current month and previous months)
    end_date = datetime.now().date().replace(day=1)
    current_date = end_date
    
    month_list = []
    for i in range(months):
        month_list.append(current_date.strftime('%Y-%m'))
        # Move to previous month
        if current_date.month == 1:
            current_date = current_date.replace(year=current_date.year - 1, month=12)
        else:
            current_date = current_date.replace(month=current_date.month - 1)
    
    # Reverse to get chronological order
    month_list.reverse()
    
    # Get occupancy data for each month
    occupancy_data = []
    
    for month in month_list:
        # Count total rooms for this property
        total_rooms = Room.query.filter_by(property_id=property_id).count()
        
        if total_rooms == 0:
            occupancy_rate = 0
        else:
            # Count occupied rooms for this month
            occupied_rooms = db.session.query(db.func.count(OccupancyRecord.id)).filter(
                OccupancyRecord.month == month,
                OccupancyRecord.is_occupied == True,
                OccupancyRecord.room_id.in_(
                    db.session.query(Room.id).filter(Room.property_id == property_id)
                )
            ).scalar() or 0
            
            # Calculate occupancy rate
            occupancy_rate = (occupied_rooms / total_rooms) * 100
        
        # Format month for display
        year, month_num = map(int, month.split('-'))
        month_name = calendar.month_name[month_num]
        display_month = f"{month_name[:3]} {year}"
        
        occupancy_data.append({
            "month": month,
            "display_month": display_month,
            "rate": round(occupancy_rate, 1)
        })
    
    response_data = {
        "property_name": property_obj.name,
        "property_id": property_obj.id,
        "occupancy_data": occupancy_data
    }
    
    return jsonify(response_data)