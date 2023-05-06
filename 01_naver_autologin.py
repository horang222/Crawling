from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyperclip
import pyautogui
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

# 웹페이지 해당 주소로 이동
driver.implicitly_wait(5) # 웹페이지가 로딩될 때까지 5초는 기다림
driver.maximize_window() # 화면창 최대화
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

# driver.find_element(By.CSS_SELECTOR, '#id').send_keys('gor456')
driver.find_element(By.CSS_SELECTOR, '#id').click()
pyperclip.copy('gor456')
pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')
time.sleep(2)

# driver.find_element(By.CSS_SELECTOR, '#pw').send_keys('cpa2020gogo!nvr')
driver.find_element(By.CSS_SELECTOR, '#pw').click()
pyperclip.copy('cpa2020gogo!nvr')
pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '#log\.login').click()