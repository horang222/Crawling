import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager # webdriver_manager 처음 실행할 때는 다운받느라 조금 시간이 걸릴 수 있음

# 브라우저 꺼짐 방지
options = Options()
options.add_experimental_option('detach', True)

# 불필요한 에러 메시지 없애기
options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 네이버 금융 코스피200 페이지 접속
url = 'https://finance.naver.com/sise/sise_index_day.nhn?code=KPI200'
driver.get(url)

# 코스피200 지수
kospi_index = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'now_value'))).text
print('코스피200 지수:', kospi_index)

# 코스피200 등락 정보
kospi_change = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'change_value_and_rate'))).text.strip()
print('코스피200 등락 정보:', kospi_change)

# 코스피200 투자자별 매매동향
try:
    investor_data = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#tab_sel3 > tr')))
except:
    print('로딩 시간이 ㅈㄴ 길어요')
    
for data in investor_data:
    category = data.find_element(By.TAG_NAME, 'th').text
    buy = data.find_element(By.CSS_SELECTOR, '.tah.p11.numbig').text
    sell = data.find_element(By.CSS_SELECTOR, '.tah.p9.numbig').text
    print(category, ':', buy, '/', sell)
