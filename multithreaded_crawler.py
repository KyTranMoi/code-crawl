import scrapy
import json
import os
import re
class CodeProjectSpider(scrapy.Spider):
    name = 'codeproject'
    #link cần crawl chỉ lick của codeproject
    start_urls = ['https://www.codeproject.com/search.aspx?q=machine+learning&doctypeid=1%3b2%3b3%3b13%3b11%3b17%3b4%3b5%3b6%3b7&ratingmin=5&pgsz=50&pgnum=1',
 'https://www.codeproject.com/search.aspx?q=machine+learning&doctypeid=1%3b2%3b3%3b13%3b11%3b17%3b4%3b5%3b6%3b7&ratingmin=5&pgsz=50&pgnum=2']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

    def parse(self, response):
        taget = response.css('div.hover-container.content-list-item.clearfix')
        for i in taget:
            link = i.css('a::attr(href)').get()
            yield response.follow(link, headers=self.headers, callback=self.parse_details)

        next_page = response.css('a.nextLink::attr(href)').get()
        if next_page:
            yield response.follow(next_page, headers=self.headers, callback=self.parse)
   
    
    def parse_details(self, response):
        title = response.xpath('.//*[@class="title"]/h1/text()').get()
        content_bug = response.xpath('.//*[@id="contentdiv"]').get()
        
        contents = re.sub(re.compile('<.*?>'),'',content_bug)
        if contents is "Dowload":
            content = re.sub(r'Download.*?\n', '', contents)
        else:
            content = contents

        if content and title:
            datas = {
                "url": response.url,
                "title": title.strip(),
                "content": content.strip(),
                "code": f"codeproject_ML_{self.tag}",
                "language": 'English',
                "tags": "ML"
            }
            self.data.append(datas)
            self.tag += 1
            self.sum_all += 1

    def __init__(self, *args, **kwargs):
        super(CodeProjectSpider, self).__init__(*args, **kwargs)
        self.data = []
        self.tag = 0
        self.sum_all = 0


    def closed(self, reason):
        if os.path.isfile('data.json'):
            #data là tên file lưu dữ liệu nếu muốn tạo nếu muốn lưu dữ liệu vào file khác thì thay data bằng tên file khác
            with open('data.json', 'r', encoding='utf-8-sig') as f: #nhớ đổi này nữa ạ
                existing_data = json.load(f)
        else:
            existing_data = []

        existing_data.extend(self.data)

        with open('data.json', 'w', encoding='utf-8-sig') as f:#nhớ đổi này nữa ạ
            json.dump(existing_data, f, indent=4, ensure_ascii=False)


