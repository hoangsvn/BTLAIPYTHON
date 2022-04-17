import os,wikipedia
from Pyaudiovn import Speak_vn,listen
def openApplication():
    Speak_vn("bạn muốn mở ứng dùng nào!")
    for i in range(3):
        app =listen()
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
    Speak_vn("tôi sẽ mở zalo ngay")
    os.startfile(r"C:\Users\Hoang\AppData\Local\Programs\Zalo\Zalo.exe")
def word():
    Speak_vn("mở word")
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
def excel():
    Speak_vn("mở excel")
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
def powerpoint():
    Speak_vn("mở powerpoint")
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
def search():
    wikipedia.set_lang('vi')
    Speak_vn("bạn cần tìm thông tin gì ạ!")
    key = listen()
    data =  wikipedia.summary(key,1)
    Speak_vn(data)