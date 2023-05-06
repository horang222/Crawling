from selenium import webdriver
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager # webdriver_manager 처음 실행할 때는 다운받느라 조금 시간이 걸릴 수 있음

# 브라우저 꺼짐 방지
options = Options()
options.add_experimental_option('detach', True)

# 불필요한 에러 메시지 없애기
options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 네이버 금융 코스피 종목코드 페이지 접속
url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1'
driver.get(url)

# 코스피 종목코드와 종목명 추출
kospi_table = driver.find_element(By.ID, 'table_wrapper_nv').find_element(By.TAG_NAME, 'tbody')
kospi_rows = kospi_table.find_elements(By.TAG_NAME, 'tr')
kospi_codes = []
kospi_names = []
for row in kospi_rows:
    code = row.find_elements(By.TAG_NAME, 'td')[1].text
    name = row.find_elements(By.TAG_NAME, 'a')[0].text
    kospi_codes.append(code)
    kospi_names.append(name)

# 코스피 종목코드와 종목명을 데이터프레임으로 만들기
kospi_df = pd.DataFrame({'종목코드': kospi_codes, '종목명': kospi_names})

# 크롬 브라우저 닫기
driver.quit()

print(kospi_df)
