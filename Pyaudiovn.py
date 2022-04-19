from re import sub
from gtts import gTTS as GT
import playsound,os,speech_recognition
Speak_Folder='Sound'
def Speak_vn(Speak):
    Sp=sub(r'[^\w\d\s]+', ' ', Speak).title().strip()
    pathsound =f'{Speak_Folder}\{Sp}.mp3'
    print("F.R.I.D.A.Y: "+Speak.title())
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
    AIlisten = 'I am sory'
    with speech_recognition.Microphone() as mic:
        print("F.R.I.D.A.Y: listening... ")
        bot.pause_threshold = 1 #dung 2s roi nghe lenh moi
        audio = bot.listen(mic)
        try:
            AIlisten=bot.recognize_google(audio, language="vi-VN")
        except speech_recognition.UnknownValueError:
            audio = bot.listen(mic)


    print("You say : "+AIlisten)
    return str(AIlisten).lower()

if __name__=='__main__':
    
    while True:
        listen()