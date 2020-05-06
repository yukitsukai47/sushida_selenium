import sys
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#寿司打のURLを記載する
url = "http://typingx0.net/sushida/play.html?soundless"
#pathには自身でダウンロードしたブラウザのドライバのパスを指定する
#path = "/Users/ユーザ名/Downloads/chromedriver"
driver = webdriver.Chrome(path)

command = True
window = (800, 1000)
driver.set_window_size(*window)
driver.get(url)
actions = ActionChains(driver)
input("キーを押すと連打が始まります")


def renda():
    while command:
        actions.send_keys("aiueobcdfghjklmnpqrstvwxyz-,!?").perform()


def kill():
    while True:
        ctrl = input('exitを入力すると連打が止まります：')
        if ctrl == "exit":
            global command
            command = False
            break
        
        else:
            command = True

            
def main():
    try:
        thread1 = threading.Thread(target=renda)
        thread2 = threading.Thread(target=kill)
        thread1.start()
        thread2.start()

    except UnexpectedAlertPresentException:
        alert = driver.switch_to_alert()
        alert.accept()
        print('問題が発生しました\n再度連打を試行します。')
        main()
        driver.close()

if __name__ == '__main__':
    main()
