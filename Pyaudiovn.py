from re import S
from gtts import gTTS as GT
import playsound,os,speech_recognition
Folder_path='Sound'
def Speak_vn(s):
    pathsound =f'{Folder_path}\{s.title()}.mp3'
    print("F.R.I.D.A.Y: "+s.title())
    try:
        playsound.playsound(pathsound,True)
    except:
        GT(text=s, lang='vi', slow=False).save(pathsound)
        playsound.playsound(pathsound,True)


def ReadHitory():
    path = f'{Folder_path}/history.txt'
    list=[]
    try:
        with open(path, 'r', encoding='UTF-8') as File:
            list=File.readlines()
    except:
        with open(path, 'a+', encoding='UTF-8') as File:
            return list
    return list
def History(string):
    path = f'{Folder_path}/history.txt'
    with open(path, 'a+', encoding='UTF-8') as File:
        File.write(string+"\n")
def listen():
    bot = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("F.R.I.D.A.Y: listening...")
        bot.pause_threshold = 1 #dung 2s roi nghe lenh moi
        audio = bot.listen(mic)
    s = ""
    try:
        s = bot.recognize_google(audio, language="vi-VN")
    except speech_recognition.UnknownValueError:
        s=''
    print("You say: "+s)
    return s.lower()
if __name__=='__main__':
    Speak_vn('Xin chào2')
    Speak_vn('Xin chào2')
    Speak_vn('Xin chào2')
    Speak_vn('Xin chào2')
    Speak_vn('Xin chào2')
    Speak_vn('Xin chào2')
    Speak_vn('Xin chào2')
    Speak_vn('Xin chào4')
    Speak_vn('Xin chào2')
    Speak_vn('Xin chào2')
    Speak_vn('Xin chào2')

    # ReadHitory()



