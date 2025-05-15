"""
Script to fix JSON serialization of Decimal objects
"""

import json
from decimal import Decimal
import re

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def fix_routes_file():
    """
    This function updates the routes.py file to handle Decimal serialization in JSON
    """
    with open('routes.py', 'r') as file:
        content = file.read()
    
    # Add import for DecimalEncoder if not already present
    if 'class DecimalEncoder' not in content:
        # Find the import section
        import_section_end = content.find('\n\n', content.find('import'))
        
        # Add DecimalEncoder import
        encoder_import = """
# Custom JSON encoder for Decimal objects
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)
"""
        
        # Insert after imports
        modified_content = content[:import_section_end] + encoder_import + content[import_section_end:]
        
        # Replace json.dumps calls with DecimalEncoder
        modified_content = re.sub(
            r'json\.dumps\(([^)]+)\)', 
            r'json.dumps(\1, cls=DecimalEncoder)', 
            modified_content
        )
        
        # Write back to file
        with open('routes.py', 'w') as file:
            file.write(modified_content)
        
        print("Successfully updated routes.py to handle Decimal serialization")
    else:
        print("DecimalEncoder is already present in routes.py")

if __name__ == "__main__":
    fix_routes_file()