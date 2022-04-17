from time import sleep
from pickle import TRUE
from Appchrome import AppChromeControler
from Pyaudiovn import listen,Speak_vn

def AICONTROLER():
    while TRUE:
        SP,T=ENDAI()
        if T:
            break
        else :
            AppChromeControler(SP)

def ENDAI():
    list=['thôi','tạm biệt','đi','biến','lướt','next','goobye']
    Speak=listen()
    if Speak in list:
        Speak_vn('Xin chào hẹn gặp lại')
        return Speak,False
    return Speak,True

if __name__=='__main__':
    AICONTROLER()