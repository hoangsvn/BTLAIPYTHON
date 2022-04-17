from pickle import TRUE
from Appchrome import AppChromeControler
from Pyaudiovn import listen,Speak_vn
from System import Systemcontroler

def AICONTROLER():
    while TRUE:
        SP,T=ENDAI()
        if T:
            if Systemcontroler(SP):
                continue
            else:
                AppChromeControler(SP)
        else :
            break

def ENDAI():
    list=['thôi','tạm biệt','đi','biến','lướt','thoát','exit','next','goobye']
    Speak=listen()
    if Speak in list:
        Speak_vn('Xin chào hẹn gặp lại')
        return Speak,False
    return Speak,True

if __name__=='__main__':
    AICONTROLER()