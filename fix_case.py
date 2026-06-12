import os
import glob

files = glob.glob('*.html') + glob.glob('services/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the exact substring
    new_content = content.replace('assets/services/', 'assets/Services/')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
