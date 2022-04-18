from pickle import TRUE
from Appchrome import AppChromeControler,googlesearch
from Pyaudiovn import listen,Speak_vn
from System import Systemcontroler
from AppPC import Applicationcontroler

def AICONTROLER():
    while TRUE:
        SP,T=ENDAI()
        if T:
            if Systemcontroler(SP)!=True:
                continue
            elif AppChromeControler(SP)!=True:
                continue
            elif Applicationcontroler(SP)!=True:
                continue
            else:
                googlesearch(SP)
        else :
            break

def ENDAI():
    list=['thôi','tạm biệt','đi','biến ','lướt','thoát','exit','next','goodbye']
    Speak=listen().lower()
    if Speak!='' and Speak in list:
        Speak_vn('Xin chào hẹn gặp lại')
        return Speak,False
    return Speak,True

if __name__=='__main__':
    AICONTROLER()