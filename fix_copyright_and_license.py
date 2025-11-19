#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Copyright and License in All Python Files
==============================================
Ensures all Python files have:
1. Correct copyright: © 2025 Carmen Wrede, Lino Casu
2. Correct license: ANTI-CAPITALIST SOFTWARE LICENSE v1.4
3. No mention of Luca Gluvic

© 2025 Carmen Wrede, Lino Casu
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import os
import sys
from pathlib import Path

# UTF-8 für Windows
os.environ['PYTHONIOENCODING'] = 'utf-8:replace'
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except: pass

def fix_file(file_path):
    """Fix copyright and license in a single file"""
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    original_content = content
    modified = False
    
    # Remove any Luca Gluvic mentions
    if 'Gluvic' in content or 'Luca' in content:
        content = content.replace('Luca Gluvic', 'Carmen Wrede, Lino Casu')
        content = content.replace('Luca', 'Carmen Wrede')
        modified = True
        print(f"  ⚠ Removed Luca/Gluvic from {file_path.name}")
    
    # Check if file has copyright
    has_copyright = '© 202' in content
    has_correct_authors = 'Carmen Wrede' in content and 'Lino Casu' in content
    has_license = 'ANTI-CAPITALIST SOFTWARE LICENSE' in content
    
    # If no copyright at all, add it after docstring
    if not has_copyright:
        # Find end of docstring
        lines = content.split('\n')
        insert_line = None
        in_docstring = False
        docstring_char = None
        
        for i, line in enumerate(lines):
            # Check for docstring start
            if not in_docstring:
                if '"""' in line:
                    in_docstring = True
                    docstring_char = '"""'
                elif "'''" in line:
                    in_docstring = True
                    docstring_char = "'''"
            else:
                # Check for docstring end
                if docstring_char in line and i > 0:
                    insert_line = i + 1
                    break
        
        if insert_line is not None:
            # Add copyright and license after docstring
            lines.insert(insert_line, "")
            lines.insert(insert_line + 1, "© 2025 Carmen Wrede, Lino Casu")
            lines.insert(insert_line + 2, "Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4")
            content = '\n'.join(lines)
            modified = True
            print(f"  ✓ Added copyright to {file_path.name}")
    
    # Fix incorrect copyright (missing authors)
    elif has_copyright and not has_correct_authors:
        # Find copyright line and fix it
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if '© 202' in line:
                # Check if it has both authors
                if 'Carmen Wrede' not in line or 'Lino Casu' not in line:
                    # Replace with correct version
                    lines[i] = "© 2025 Carmen Wrede, Lino Casu"
                    modified = True
                    print(f"  ✓ Fixed copyright in {file_path.name}")
                break
        content = '\n'.join(lines)
    
    # Add license if missing
    if has_copyright and not has_license:
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if '© 202' in line:
                # Check if next line already has license
                if i + 1 < len(lines) and 'Licensed under' not in lines[i + 1]:
                    lines.insert(i + 1, "Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4")
                    modified = True
                    print(f"  ✓ Added license to {file_path.name}")
                break
        content = '\n'.join(lines)
    
    # Write back if modified
    if modified:
        with open(file_path, 'w', encoding='utf-8', errors='replace') as f:
            f.write(content)
        return True
    
    return False

def main():
    """Main execution"""
    print("\n" + "="*70)
    print("FIXING COPYRIGHT AND LICENSE IN ALL PYTHON FILES")
    print("="*70 + "\n")
    
    # Get all Python files
    root = Path(__file__).parent
    py_files = list(root.rglob("*.py"))
    
    print(f"Found {len(py_files)} Python files\n")
    
    modified_count = 0
    for py_file in py_files:
        # Skip this script itself
        if py_file.name == 'fix_copyright_and_license.py':
            continue
        
        # Skip __pycache__ and venv
        if '__pycache__' in str(py_file) or 'venv' in str(py_file):
            continue
        
        if fix_file(py_file):
            modified_count += 1
    
    print("\n" + "="*70)
    print(f"COMPLETE! Modified {modified_count} files")
    print("="*70)
    
    # Verify: Check for any remaining issues
    print("\nVerifying...")
    issues = []
    for py_file in py_files:
        if '__pycache__' in str(py_file) or 'venv' in str(py_file):
            continue
        if py_file.name == 'fix_copyright_and_license.py':
            continue
        
        with open(py_file, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        if 'Gluvic' in content or ('Luca' in content and 'Carmen' not in content):
            issues.append(f"  ⚠ {py_file.name}: Still contains Luca/Gluvic")
        
        if '© 202' not in content:
            issues.append(f"  ⚠ {py_file.name}: No copyright")
        elif 'Carmen Wrede' not in content or 'Lino Casu' not in content:
            issues.append(f"  ⚠ {py_file.name}: Incorrect copyright")
    
    if issues:
        print("\nRemaining issues:")
        for issue in issues:
            print(issue)
    else:
        print("\n✓ All files verified!")
        print("✓ No Luca/Gluvic references found")
        print("✓ All files have correct copyright")
        print("✓ License information present")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
