from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from colorama import Fore
import os

options = Options()
#options.add_argument("--headless")
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1}) # 알림 허용 차단 묻는거 끄기
chrome = Service("./StorySpam/chromedriver.exe")
driver = webdriver.Chrome(service=chrome, options=options)

def Login(account,pw_):
    try:
        driver.get("https://ko-kr.facebook.com/")
        email = driver.find_element(By.XPATH, '//*[@id="email"]')  
        email.send_keys(account)
        
        pw = driver.find_element(By.XPATH, '//*[@id="pass"]')
        pw.send_keys(pw_)

        login = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
        login.click()

        print(f"{Fore.GREEN}[SUCCESS] : LOGIN SUCCESS{Fore.RESET}")
        return True
    except Exception as e:
        print()
        input("[ERROR] - 로그인 도중 오류가 발생 하였습니다.")
        return False
    
    

def isStorySpam(count,msg,account,pw_):
    Set = Login(account,pw_)
    if Set == True:
        count = int(count)
        cnt = 0
        if count >= 20:
            return input("스토리 생성 횟수는 20회 이상이면 안됩니다.")
        for _ in range(count):
            sleep(1)
            driver.get("https://www.facebook.com/stories/create/")

            sleep(1)
            text_story_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]')
            text_story_btn.click()
            sleep(1)
            text_area = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/div[1]/div/label/div/div/textarea')
            text_area.send_keys(msg)

            upload_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div')
            upload_btn.click()
            cnt += 1
            print(f"{Fore.GREEN}[SUCCESS] : STORY SPAM SUCCESS | {cnt} | {msg} {Fore.RESET}")

            sleep(1.3)
            driver.get("https://www.facebook.com/")
        driver.quit()
        os.system("cls")
        return True
    else:
        return input("알 수 없는 오류가 발생하였습니다.")
    


