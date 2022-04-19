from re import sub
from gtts import gTTS as GT
import playsound,os,speech_recognition
Speak_Folder='Sound'
def Speak_vn(Speak):
    Sp=sub(r'[^\w\d\s]+', ' ', Speak).title().strip()
    pathsound =f'{Speak_Folder}\{Sp}.mp3'
    print("F.R.I.D.A.Y: "+str(Speak).title())
    try:
        playsound.playsound(pathsound,True)
    except:
        try:
            GT(text=Speak, lang='vi', slow=False).save(pathsound)
        except:
            os.mkdir(Speak_Folder)
            GT(text=Speak, lang='vi', slow=False).save(pathsound)
        playsound.playsound(pathsound,True)

def listen():
    bot = speech_recognition.Recognizer()
    Mod=0
    with speech_recognition.Microphone() as mic:
        print("F.R.I.D.A.Y: listening... ")
        bot.pause_threshold = 1 #dung 2s roi nghe lenh moi
        audio = bot.listen(mic)
        try:
            AIlisten=bot.recognize_google(audio, language="vi-VN")
        except:
            Mod=1
            AIlisten = 'I am sorry'
    if Mod==1:
        print("F.R.I.D.A.Y: "+AIlisten.title())
    else:
        print("You say : "+AIlisten.title())
    return str(AIlisten).lower()

if __name__=='__main__':
    
    while True:
        listen()