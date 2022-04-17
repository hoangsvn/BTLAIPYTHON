from selenium import webdriver
import webbrowser, security ,botfb
from pickle import TRUE
from time import sleep
from Time import time,date
from Pyaudiovn import Speak_vn,listen
from AppPC import openApplication,search
def AppChromeControler():
    while TRUE:
        s = listen()
        if("google" in s):
            google()
        elif("youtube" in s):
            youtube()
        elif ("facebook" in s):
            facebook()
        elif ("gmail" in s or "thư" in s):
            gmail()
        elif ("giờ" in s):
            Speak_vn(time())
        elif("ngày" in s):
            Speak_vn(date())
        elif("application" in s or "ứng dụng" in s):
            openApplication()
        elif("tìm kiếm" in s or "thông tin" in s):
            search()

def google():
    Speak_vn("bạn muốn tìm gì trên google ạ?")
    search = listen().lower()
    url = f"https://www.google.com/search?q={search}"
    webbrowser.get().open(url)
    Speak_vn(f'vâng!! tôi sẽ tìm {search} trên google ngay')
def youtube():
    Speak_vn("bạn muốn xem gì trên youtube ?")
    search = listen()
    url = f"https://www.youtube.com/?q={search}"
    webbrowser.get().open(url)
    Speak_vn(f'vâng! tôi sẽ tìm {search} trên youtube')
def facebook():
    Speak_vn("mở facebook")
    browser = webdriver.Chrome('.\chromedriver.exe')
    # mỏ facebook
    botfb.open_facebook(security.USERNAME,security.PASSWORD,browser)
    sleep(6.5)
    # if("trang chủ" in s or "home" in s or "bảng tin" in s):
    while True:
        s = listen()
        if("tìm kiếm" in s or "search" in s):
            Speak_vn("bạn muốn tôi tìm kiếm gì nào")
            key = listen()
            while(key == ""):
                key = listen()    
            botfb.search_facebook(browser,key)
            sleep(10)
        elif("đóng" in s or "dừng" in s or "thôi" in s or "rừng" in s):
            Speak_vn("bạn có muốn đóng facebook không?")
            ok = listen()
            # for i in range(0,2):
            #     if(ok!=""):
            #         break

            if("có" in ok or "yes" in ok):
                print("có")
                browser.close()
            else:
                print("không")
            break
    # speak_vn("bạn mở facebook để xem bảng tin hay tìm bạn bè ạ")
    # key = listen()
    # url = f"https://www.facebook.com/"
    # if("bạn bè" in key):
    #     speak_vn("tên nick bạn muốn tìm là gì vây")
    #     nick = listen()
    #     url = f"https://www.facebook.com/search/top?q={nick}"
    # webbrowser.get().open(url)
def gmail():
    url = f"https://mail.google.com/mail/u/0/#inbox"
    webbrowser.get().open(url)
