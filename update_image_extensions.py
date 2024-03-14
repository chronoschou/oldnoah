import re

# 讀取HTML文件
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# 使用正則表達式替換 assets/img/team 目錄下所有的 .png 圖片引用為 .jpg
modified_html_content = re.sub(r'(assets/img/portfolio/[\w-]+)\.webp', r'\1.png', html_content)

# 將修改後的HTML內容寫回文件
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(modified_html_content)

print("HTML文件中assets/img/team路徑下所有圖片的副檔名已從.png更改為.jpg。")