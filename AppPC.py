import os,wikipedia
from Pyaudiovn import Speak_vn,listen
def openApplication():
    Speak_vn("bạn muốn mở ứng dùng nào!")
    for i in range(3):
        app =listen().split()
        if("zalo" in app):
            zalo()
        elif("word" or "soạn" and "thảo" and "văn" and "bản" in app):
            word()
        elif("excel" or "trang" and "tính" in app):
            excel()
        elif("powerpoint" or "trình" and "chiếu" or "chình" and "chiếu" in app):
            powerpoint()
        else:
            Speak_vn("ứng dụng chưa được cài đặt")


def zalo():
    Speak_vn("tôi sẽ mở zalo ngay")
    try:
        os.startfile(r"C:\Users\Hoang\AppData\Local\Programs\Zalo\Zalo.exe")
    except:
        Speak_vn('Ứng dụng chưa cài đặt')
def word():
    Speak_vn("mở word")
    try:
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
    except:
        Speak_vn('Ứng dụng chưa cài đặt')
def excel():
    Speak_vn("mở excel")
    try:
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
    except:
        Speak_vn('Ứng dụng chưa cài đặt')
def powerpoint():
    Speak_vn("mở powerpoint")
    try:
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
    except:
        Speak_vn('Ứng dụng chưa cài đặt')
def search():
    wikipedia.set_lang('vi')
    Speak_vn("bạn cần tìm thông tin gì ạ!")
    key = listen()
    data =  wikipedia.summary(key,1)
    Speak_vn(data)