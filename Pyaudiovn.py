from re import S
from gtts import gTTS as GT
import playsound,os,speech_recognition
Folder_path='Sound'
def Speak_vn(s):
    pathsound =f'{Folder_path}\{s}.mp3'
    print("F.R.I.D.A.Y: "+s.title())
    if pathsound in ReadHitory():
        playsound.playsound(pathsound,True)
    else :
        try:
            GT(text=s, lang='vi', slow=False).save(pathsound)
        except:
            os.mkdir(Folder_path)
        History(pathsound)
        playsound.playsound(pathsound,True)

def ReadHitory():
    path = f'{Folder_path}/history.txt'
    list=[]
    with open(path, 'r', encoding='UTF-8') as File:
        list=File.readlines()
    return list
def History(string):
    path = f'{Folder_path}/history.txt'
    with open(path, 'a+', encoding='UTF-8') as File:
        File.write(string)
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
    # ReadHitory()



