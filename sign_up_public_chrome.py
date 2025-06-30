from selenium import webdriver  # 用于操作浏览器
from selenium.webdriver.chrome.options import Options   # 用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service   # 用于管理谷歌驱动
import time
from selenium.webdriver.common.by import By
from plyer import notification

user = []

def she():
    q1 = Options()
    q1.add_argument('--headless=new')
    q1.add_argument('--no-sandox')
    q1.add_experimental_option('detach', True)
    a1 = webdriver.Chrome(service=Service('chromedriver.exe'), \
                          options=q1)
    a1.implicitly_wait(3)
    return a1

def input_passworld():
    try:
        a1 = she()
        a1.get('http://10.255.200.11/')
        #下面输入学号，密码，选择电信
        a1.find_element(By.XPATH, '//*[@id="domain"]'\
                        ).click()
        if user[2] == '1':
            a1.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[3]/div[1]/div[3]/select/option[1]' \
                            ).click()
        elif user[2] == '2':
            a1.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[3]/div[1]/div[3]/select/option[2]'\
                            ).click()
        else :
            a1.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[3]/div[1]/div[3]/select/option[3]' \
                            ).click()
        a1.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[3]/div[1]/div[1]/input' \
                        ).send_keys(user[0])
        a1.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[3]/div[1]/div[2]/input' \
                        ).send_keys(user[1])
        #点击确认
        a1.find_element(By.XPATH, '//*[@id="loginBtn"]'\
                        ).click()
        a1.minimize_window()
        #发送通知
        send_notification()
    except:
        notification.notify(
            title="自动登录校园网",
            message="登录失败！！！\n或者已经登录！",
            timeout=5,  # 通知显示时间（秒）
        )
    return 0

def read_user_inf():
    with open('user.txt', encoding='utf-8') as file:
       for line in file:
           user.append(line.rstrip())    #循环把txt的内容加入到列表中


def send_notification():
    notification.notify(
        title="自动登录校园网",
        message="成功！",
        timeout=5,  # 通知显示时间（秒）
    )

def main():
    read_user_inf()
    print(user)
    input_passworld()

    return 0

main()



