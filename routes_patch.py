
# ==== ROOM STATS FUNCTION ====
def room_stats():
    try:
        import matplotlib
        matplotlib.use('Agg')  # Non-interactive backend
        import matplotlib.pyplot as plt
        from matplotlib.ticker import FuncFormatter
        
        # Regular implementation with matplotlib
        # (existing code...)
    except (ImportError, NameError):
        # Fallback to no-graph version
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
            
        # Check if user has access to this property
        if not current_user.is_admin:
            has_access = False
            for prop in accessible_properties:
                if prop.id == property_id:
                    has_access = True
                    break
            if not has_access:
                flash('Anda tidak memiliki akses ke properti ini', 'danger')
                return redirect(url_for('reports'))
        
        # Get property details
        property_obj = Property.query.get_or_404(property_id)
        
        # Get rooms for this property
        rooms = Room.query.filter_by(property_id=property_id).all()
        
        # Get occupancy data for the selected month
        occupied_rooms = OccupancyRecord.query.filter(
            OccupancyRecord.room_id.in_([r.id for r in rooms]),
            OccupancyRecord.month == month,
            OccupancyRecord.is_occupied == True
        ).count()
        
        total_rooms = len(rooms)
        occupancy_rate = (occupied_rooms / total_rooms * 100) if total_rooms > 0 else 0
        
        # Get room type statistics
        room_types_data = []
        room_types = ['Standard', 'Eksekutif']  # Define the two room types
        
        for room_type in room_types:
            rooms_of_type = [r for r in rooms if r.room_type == room_type]
            total_of_type = len(rooms_of_type)
            
            if total_of_type > 0:
                occupied_of_type = OccupancyRecord.query.filter(
                    OccupancyRecord.room_id.in_([r.id for r in rooms_of_type]),
                    OccupancyRecord.month == month,
                    OccupancyRecord.is_occupied == True
                ).count()
                
                occupancy_rate_of_type = (occupied_of_type / total_of_type * 100) if total_of_type > 0 else 0
                
                room_types_data.append({
                    'type': room_type,
                    'total': total_of_type,
                    'occupied': occupied_of_type,
                    'occupancy_rate': occupancy_rate_of_type
                })
        
        return render_template(
            'room_stats_no_graph.html',
            property=property_obj,
            month=month,
            rooms=rooms,
            total_rooms=total_rooms,
            occupied_rooms=occupied_rooms,
            occupancy_rate=occupancy_rate,
            properties=accessible_properties,
            room_types_data=room_types_data
        )

# ==== FINANCIAL STATS FUNCTION ====
def financial_stats():
    try:
        import matplotlib
        matplotlib.use('Agg')  # Non-interactive backend
        import matplotlib.pyplot as plt
        from matplotlib.ticker import FuncFormatter
        
        # Regular implementation with matplotlib
        # (existing code...)
    except (ImportError, NameError):
        # Fallback to no-graph version
        # Get property ID from request or default to first accessible property
        property_id = request.args.get('property_id', None)
        year = request.args.get('year', str(datetime.now().year))
        
        # Get accessible properties for current user
        accessible_properties = get_user_properties()
        accessible_property_ids = [prop.id for prop in accessible_properties]
        
        if not accessible_properties:
            flash('Anda tidak memiliki akses ke properti manapun', 'danger')
            return redirect(url_for('reports'))
            
        if property_id is None:
            property_id = accessible_properties[0].id
        else:
            property_id = int(property_id)
            
        # Check if user has access to this property
        if not current_user.is_admin and property_id not in accessible_property_ids:
            flash('Anda tidak memiliki akses ke properti ini', 'danger')
            return redirect(url_for('reports'))
        
        # Get property details
        property_obj = Property.query.get_or_404(property_id)
        
        # Process financial data by month
        monthly_data = []
        yearly_income = 0
        yearly_expense = 0
        
        for i in range(1, 13):
            start_date = date(int(year), i, 1)
            if i == 12:
                end_date = date(int(year) + 1, 1, 1)
            else:
                end_date = date(int(year), i + 1, 1)
            
            # Query income and expense
            if current_user.is_admin:
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
            else:
                income = db.session.query(db.func.sum(FinancialRecord.amount)).filter(
                    FinancialRecord.transaction_type == 'income',
                    FinancialRecord.transaction_date >= start_date,
                    FinancialRecord.transaction_date < end_date,
                    FinancialRecord.property_id == property_id,
                    FinancialRecord.property_id.in_(accessible_property_ids)
                ).scalar() or 0
                
                expense = db.session.query(db.func.sum(FinancialRecord.amount)).filter(
                    FinancialRecord.transaction_type == 'expense',
                    FinancialRecord.transaction_date >= start_date,
                    FinancialRecord.transaction_date < end_date,
                    FinancialRecord.property_id == property_id,
                    FinancialRecord.property_id.in_(accessible_property_ids)
                ).scalar() or 0
            
            profit = income - expense
            
            monthly_data.append({
                'month': calendar.month_name[i],
                'income': income,
                'expense': expense,
                'profit': profit
            })
            
            yearly_income += income
            yearly_expense += expense
        
        yearly_profit = yearly_income - yearly_expense
        
        return render_template(
            'financial_stats_no_graph.html',
            property=property_obj,
            year=year,
            properties=accessible_properties,
            monthly_data=monthly_data,
            yearly_income=yearly_income,
            yearly_expense=yearly_expense,
            yearly_profit=yearly_profit
        )
