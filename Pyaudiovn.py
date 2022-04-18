from re import S
from gtts import gTTS as GT
import playsound,os,speech_recognition
Speak_Folder='Sound'
def Speak_vn(Speak):
    Sp=str(Speak).strip('*\/?":><|').title()
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
    Speak_vn('Xin chào1')
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



