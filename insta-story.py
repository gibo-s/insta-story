
#ログインアカウント情報の入力
login_id = ''
login_password = ''

#Seleniumのインストール
!pip install selenium

#webdriverのインストール
from selenium import webdriver

#sleepメソッドのインポート
from time import sleep

#webdriver managerのインストール・インポート
!pip install webdriver_manager
sleep(3)
from webdriver_manager.chrome import ChromeDriverManager

#ブラウザ立ち上げ
browser = webdriver.Chrome(ChromeDriverManager().install())

#Instagramを開く
browser.get('https://www.instagram.com/')

sleep(3)

#ユーザー名の入力
user_name = browser.find_element_by_name('username')
user_name.send_keys(login_id)

#パスワードの入力
user_password = browser.find_element_by_name('password')
user_password.send_keys(login_password)

#ログインボタンを押す
login_button = browser.find_elements_by_tag_name('button')[1]
login_button.click()

sleep(3)

#ログイン情報を保存するかどうかの処理
atode_button = browser.find_elements_by_tag_name('button')[1]
atode_button.click()

sleep(2)

#通知を受け取るかどうかの処理
atode2_button = browser.find_element_by_class_name('aOOlW')
atode2_button.click()

sleep(2)

#ストーリーを閲覧する
story_button = browser.find_elements_by_class_name('OE3OK')[0]
if story_button:
    story_button.click()
    
sleep(1)
    
#ストーリーがある限り次へボタンを押して送る
next_button = browser.find_element_by_class_name('FhutL')
while True:
    next_button.click()
    sleep(1)
