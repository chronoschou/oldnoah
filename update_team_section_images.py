from bs4 import BeautifulSoup

# 讀取HTML文件
with open(r'D:\澤諾創藝\Andy_Project\noahbuilders_website\noah.github.io\index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 定位到Team Section底下的<div class="row">
team_section = soup.find('section', id='team')
row_div = team_section.find('div', class_='row') if team_section else None

if row_div:
    # 找到所有圖片元素
    imgs = row_div.find_all('img')
    existing_imgs = {int(img['src'].split('/')[-1].split('.')[0]) for img in imgs if 'team' in img['src']}
    
    # 計算缺失的圖片數量並添加
    all_needed_imgs = set(range(2, 37))
    missing_imgs = all_needed_imgs - existing_imgs
    
    for i in sorted(missing_imgs):
        new_member_html = f'''
        <div class="col-lg-3 col-md-6 d-flex align-items-stretch">
          <div class="member" data-aos="fade-up" data-aos-delay="100">
            <div class="member-img">
              <img src="assets/img/team/{i}.jpg" class="img-fluid" alt="">
              <div class="social">
                <a href=""><i class="bi bi-twitter"></i></a>
                <a href=""><i class="bi bi-facebook"></i></a>
                <a href=""><i class="bi bi-instagram"></i></a>
                <a href=""><i class="bi bi-linkedin"></i></a>
              </div>
            </div>
          </div>
        </div>
        '''
        row_div.append(BeautifulSoup(new_member_html, 'html.parser'))

# 將修改後的HTML內容寫回文件
with open(r'D:\澤諾創藝\Andy_Project\noahbuilders_website\noah.github.io\index_modified.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))

print("HTML 文件中所有圖片引用已成功更新，並且缺失的圖片引用已添加。")
