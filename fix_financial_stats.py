#!/usr/bin/env python3
# Script untuk memperbaiki fungsi financial_stats pada routes.py

import re

with open('routes.py', 'r') as f:
    content = f.read()

# Pattern untuk mencari fungsi financial_stats
pattern = r"@app.route\('/financial_stats'\)[^@]*?def financial_stats\(\):(.*?)(?=@app\.route|$)"
match = re.search(pattern, content, re.DOTALL)

if match:
    old_function = match.group(0)
    
    # Buat fungsi baru yang hanya berisi redirect
    new_function = """@app.route('/financial_stats')
@login_required
def financial_stats():
    # Redirect to Chart.js version to prevent matplotlib recursion errors
    property_id = request.args.get('property_id', None)
    year = request.args.get('year', str(datetime.now().year))
    
    # Build query parameters
    query_params = {}
    if property_id:
        query_params['property_id'] = property_id
    if year:
        query_params['year'] = year
    
    # Redirect to the Chart.js version
    return redirect(url_for('financial_stats_js', **query_params))
"""
    
    # Ganti fungsi lama dengan fungsi baru
    fixed_content = content.replace(old_function, new_function)
    
    # Simpan perubahan
    with open('routes.py', 'w') as f:
        f.write(fixed_content)
    
    print("Fungsi financial_stats berhasil diperbaiki!")
else:
    print("Fungsi financial_stats tidak ditemukan!")
