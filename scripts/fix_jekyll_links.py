import os
import re

def fix_links():
    base_dir = 'docs'
    # Walk through all directories in docs
    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Calculate relative path from current file's dir to docs root
                # e.g. docs/aulas -> ..
                # e.g. docs -> .
                
                rel_to_root = os.path.relpath(base_dir, root)
                if rel_to_root == '.':
                    path_prefix = ''
                else:
                    path_prefix = rel_to_root.replace('\\', '/') + '/'
                
                # Fix 1: [Voltar ao Início](/) -> [Voltar ao Início](../index.md)
                # We target ](/) specifically.
                
                # If path_prefix is empty, it becomes index.md
                # If path_prefix is ../, it becomes ../index.md
                
                replacement_root = f"]({path_prefix}index.md)"
                new_content = content.replace("](/", replacement_root)
                
                # Fix 2: /aulas/aula-XX -> relative path
                # Pattern: ](/subdir/file)
                # We want: ](../subdir/file) or similar
                
                # We can use regex to find all absolute links starting with /
                # and prepend path_prefix.
                # However, valid absolute URLs (http) shouldn't be touched.
                # Regex: \]\(\/(?!\/) matches ](/...) but not ](//...)
                
                def replace_absolute(match):
                    # match.group(1) is the path after /
                    path = match.group(1)
                    # If it ends with /, likely a directory index?
                    # MkDocs prefers index.md
                    
                    # We simply prepend relative prefix.
                    # /aulas/aula-09 -> ../aulas/aula-09
                    
                    return f"]({path_prefix}{path}"
                
                new_content = re.sub(r'\]\(\/(?!/)([^)]+)', replace_absolute, new_content)
                
                # Fix 3: Ensure .md extension for internal links if missing?
                # Many might be aula-09 without .md
                # Valid for MkDocs but strict mode might complain or not.
                # Let's trust MkDocs handles extensionless links if they match filenames.
                # But typically [Link](file) implies file.
                
                if content != new_content:
                    print(f"Fixing {filepath}")
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)

if __name__ == '__main__':
    fix_links()
