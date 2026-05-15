import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

img_index = 1
def get_next_img():
    global img_index
    img = f'images/saouce ({img_index}).jpg'
    img_index += 1
    if img_index > 15:
        img_index = 1
    return img

src_pattern = re.compile(r'(<img[^>]+src=[\'\"])(http[^>\"\']*?|Images\\[^>\"\']*?)([\'\"])', re.IGNORECASE)

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    def replacer(match):
        return match.group(1) + get_next_img() + match.group(3)
        
    new_content = src_pattern.sub(replacer, content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated {f}')
