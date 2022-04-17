from time import sleep
from Appchrome import AppChromeControler
from Pyaudiovn import listen,Speak_vn

def AICONTROLER():
    while ENDAI():
        AppChromeControler()
def ENDAI():
    list=['thôi','tạm biệt','đi','biến','lướt','next','goobye']
    if listen() in list:
        Speak_vn('Xin chào hẹn gặp lại')
        sleep(5)
        return False
    return True

if __name__=='__main__':
    AICONTROLER()