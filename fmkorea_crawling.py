from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager # webdriver_manager 처음 실행할 때는 다운받느라 조금 시간이 걸릴 수 있음

# 브라우저 꺼짐 방지
options = Options()
options.add_experimental_option('detach', True)

# 불필요한 에러 메시지 없애기
options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

data_t = []
data_c = []
data_l = []

for page_no in range(1, 51):
    url = f'https://www.fmkorea.com/index.php?mid=best&page={page_no}'
    driver.get(url)
    time.sleep(3)

    a_tags = driver.find_elements(By.CLASS_NAME, 'hotdeal_var8')
    categories = driver.find_elements(By.CLASS_NAME, 'category')

    if page_no != 1:
        titles = [a.text.strip() for a in a_tags]
        data_t += titles
        categories = [cate.text.strip() for cate in categories]
        data_c += categories
        links = [a.get_attribute('href') for a in a_tags]
        data_l += links
    else:    
        titles = [a.text.strip() for a in a_tags]
        titles = titles[4:]
        data_t += titles
        categories = [cate.text.strip() for cate in categories]
        categories = categories[3:]
        data_c += categories
        links = [a.get_attribute('href') for a in a_tags]
        links = links[4:]
        data_l += links

driver.quit()

import pandas as pd

df = pd.DataFrame()

df['제목'] = data_t
df['카테고리'] = data_c
df['링크'] = data_l

df.to_csv('./fmkorea.csv',encoding='utf-8', index=False)
print('데이터프레임 생성 완료!!!')