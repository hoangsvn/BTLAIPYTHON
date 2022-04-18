from selenium import webdriver
import webbrowser, security ,botfb,wikipedia
from time import sleep
from Time import time,date
from Pyaudiovn import Speak_vn,listen
def AppChromeControler(SP):
    if("google" in SP):
        google()
        return False
    elif("youtube" in SP):
        youtube()
        return False
    elif ("facebook" in SP):
        facebook()
        return False
    elif ("gmail" in SP or "thư" in SP):
        gmail()
        return False
    elif ("driver" in SP or "google driver" in SP):
        Driver()
        return False
    elif ("giờ" in SP):
        Speak_vn(time())
        return False
    elif("ngày" in SP):
        Speak_vn(date())
        return False
    elif("tìm kiếm" in SP or "thông tin" in SP):
        search()
        return False
    return True
    
def Driver():
    webbrowser.get().open('https://drive.google.com')
    Speak_vn("Vâng! tôi đang mở Driver ?")

def googlesearch(SP):
    if SP!='':
        url = f"https://www.google.com/search?q={SP.replace(' ','+')}"
        webbrowser.get().open(url)
        Speak_vn('Đang tìm kiếm trên Google')
    
def google():
    Speak_vn("bạn muốn tìm gì trên google ạ?")
    search = listen().lower()
    url = f"https://www.google.com/search?q={search.replace(' ','+')}"
    webbrowser.get().open(url)
    Speak_vn(f'vâng!! tôi sẽ tìm {search} trên google ngay')
def youtube():
    Speak_vn("Đang mở YouTube ")
    url='https://www.youtube.com'
    webbrowser.get().open(url)
    Speak_vn("Bạn muốn xem gì trên youtube ?")
    search = listen()
    if ('không' or 'no') not in search:
        url = f"https://www.youtube.com/results?search_query={search.replace(' ','+')}"
        webbrowser.get().open(url)
        Speak_vn(f'Vâng! tôi sẽ tìm {search} trên youtube')

def facebook():
    Speak_vn("Đang mở facebook")
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
    url = f"https://mail.google.com"
    webbrowser.get().open(url)
    Speak_vn("Vâng! tôi đang mở Gmail ?")
def search():
    wikipedia.set_lang('vi')
    Speak_vn("bạn cần tìm thông tin gì ạ!")
    key = listen()
    data =  wikipedia.summary(key,1)
    Speak_vn(data)
