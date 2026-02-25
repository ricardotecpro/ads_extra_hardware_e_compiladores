import os
import re
import yaml

def add_headers():
    base_dir = 'docs'
    # Walk through all directories in docs
    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for frontmatter
                if content.startswith('---\n'):
                    try:
                        # Find end of frontmatter
                        end_idx = content.find('\n---\n', 4)
                        if end_idx != -1:
                            frontmatter_raw = content[4:end_idx]
                            frontmatter = yaml.safe_load(frontmatter_raw)
                            
                            title = frontmatter.get('title')
                            layout = frontmatter.get('layout') # Jekyll specific
                            
                            # Check if H1 exists in content (after frontmatter)
                            body = content[end_idx+5:]
                            if not re.search(r'^#\s+', body, re.MULTILINE):
                                if title:
                                    print(f"Adding header to {filename}")
                                    # Add header
                                    new_body = f"# {title}\n\n{body}"
                                    
                                    # Optional: Remove layout from frontmatter or remove frontmatter if only layout/title?
                                    # MkDocs uses meta plugin for title, so keeping frontmatter is fine, just maybe remove layout.
                                    # But to be safe and clean, let's keep frontmatter for now but add H1.
                                    # The user said "remove Jekyll". 'layout' is Jekyll.
                                    
                                    # Let's remove 'layout' line from frontmatter.
                                    new_frontmatter_lines = []
                                    for line in frontmatter_raw.split('\n'):
                                        if not line.strip().startswith('layout:'):
                                            new_frontmatter_lines.append(line)
                                    
                                    new_frontmatter_str = '\n'.join(new_frontmatter_lines)
                                    
                                    new_content = f"---\n{new_frontmatter_str}\n---\n\n{new_body}"
                                    
                                    with open(filepath, 'w', encoding='utf-8') as f:
                                        f.write(new_content)
                    except Exception as e:
                        print(f"Error processing {filename}: {e}")

if __name__ == '__main__':
    add_headers()
