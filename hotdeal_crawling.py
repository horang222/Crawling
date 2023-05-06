from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager # webdriver_manager 처음 실행할 때는 다운받느라 조금 시간이 걸릴 수 있음

# 브라우저 꺼짐 방지
options = Options()
options.add_experimental_option('detach', True)

# 불필요한 에러 메시지 없애기
options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

data = []

for page_no in range(1, 11):
    url = f'https://www.fmkorea.com/index.php?mid=hotdeal&page={page_no}'
    driver.get(url)
    time.sleep(3)

    tits = driver.find_elements(By.CLASS_NAME, 'hotdeal_var8')
    infos = driver.find_elements(By.CLASS_NAME, 'hotdeal_info')

    for tit, info_list in zip(tits, infos):
        record = []
        title = tit.text.strip()
        link = tit.get_attribute('href')
        record += [title]

        info_list = info_list.text.split('/')
        
        mall = info_list[0].split(':')[-1].strip()
        price = info_list[1].split(':')[-1].strip()
        delivery = info_list[2].split(':')[-1].strip()

        product_info = [mall, price, delivery, link]
        record += product_info
        data.append(record)

driver.quit()

cols = ['글 제목', '쇼핑몰', '가격', '배송비', '링크']
df = pd.DataFrame(data, columns=cols)
print('데이터프레임 생성 완료!!!')

df.to_csv('./hotdeal.csv',encoding='utf-8', index=False)
print('데이터프레임 저장 완료!!!')