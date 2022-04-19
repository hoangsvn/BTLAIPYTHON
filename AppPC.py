import os
from Pyaudiovn import Speak_vn,listen
def Applicationcontroler(app):
    if("zalo" in app):
        zalo()
        return False
    elif("word" in app or "soạn thảo văn bản" in app):
        word()
        return False
    elif("excel" in app or "trang tính" in app):
        excel()
        return False
    elif("powerpoint" in app or "trình chiếu" in app or "chình chiếu" in app):
        powerpoint()
        return False
    return True


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
