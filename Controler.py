from Appchrome import AppChromeControler,googlesearch
from Pyaudiovn import listen,Speak_vn
from System import Systemcontroler
from AppPC import Applicationcontroler

def AICONTROLER():
    while True:
        SP=ENDAI()
        if Systemcontroler(SP)!=True:
            continue
        elif AppChromeControler(SP)!=True:
            continue
        elif Applicationcontroler(SP)!=True:
            continue
        else:
            googlesearch(SP)
            
def ENDAI():
    list=['thôi','tạm biệt','đi','biến ','lướt','thoát','exit','next','goodbye']
    Speak=listen().lower()
    if  Speak in list:
        Speak_vn('Xin chào hẹn gặp lại')
        raise SystemExit(0)
    return Speak

if __name__=='__main__':
    AICONTROLER()