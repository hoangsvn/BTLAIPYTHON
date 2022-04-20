from Appchrome import AppChromeControler
from Pyaudiovn import listen,Speak_vn
from System import Systemcontroler
from AppPC import Applicationcontroler

            
def ENDAI(SP):
    list=['thôi','tạm biệt','thoát','exit','goodbye']
    for i in list:
        if i in SP:
            return True
    return False

def Runquery(SP):
    Systemcontroler(SP)
    AppChromeControler(SP)
    Applicationcontroler(SP)

def Runing():
    Mode=0
    while True:
        Speak=listen()
        if Mode==0 and 'máy tính' in Speak:
            Speak=str(Speak).replace('máy tính',' ',1)
            Mode=1
        elif Mode==1:
            if ENDAI(Speak):
                Mode=0
                Speak_vn('Hảy gọi máy tính tôi sẻ chở lại :')
            else:
                Runquery(Speak)
        
if __name__=='__main__':
    Runing()