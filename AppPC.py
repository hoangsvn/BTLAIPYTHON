import os,wikipedia
from Pyaudiovn import Speak_vn,listen
def openApplication():
    Speak_vn("Bạn muốn mở ứng dùng nào!")
    for i in range(3):
        app =listen().lower().split()
        if("zalo" in app):
            zalo()
        elif("word" in app or "soạn thảo văn bản" in app):
            word()
        elif("excel" in app or "trang tính" in app):
            excel()
        elif("powerpoint" in app or "trình chiếu" in app or "chình chiếu" in app):
            powerpoint()
        else:
            Speak_vn("ứng dụng chưa được cài đặt")


def zalo():
    Speak_vn("Tôi sẽ mở zalo ngay")
    try:
        os.startfile(r"C:\Users\Hoang\AppData\Local\Programs\Zalo\Zalo.exe")
    except:
        Speak_vn('Ứng dụng chưa cài đặt')
def word():
    Speak_vn("Đang mở word")
    try:
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
    except:
        Speak_vn('Ứng dụng chưa cài đặt')
def excel():
    Speak_vn("Đang mở excel")
    try:
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
    except:
        Speak_vn('Ứng dụng chưa cài đặt')
def powerpoint():
    Speak_vn("Đang mở powerpoint")
    try:
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
    except:
        Speak_vn('Ứng dụng chưa cài đặt')
