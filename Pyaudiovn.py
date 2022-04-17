from gtts import gTTS as GT
import playsound,os,speech_recognition

def Speak_vn(s):
    pathsound ='Sound\speech.mp3'
    print("F.R.I.D.A.Y: "+s.title())
    try:
        GT(text=s, lang='vi', slow=False).save(pathsound)
    except:
        os.mkdir('Sound')
        GT(text=s, lang='vi', slow=False).save(pathsound)
    playsound.playsound(pathsound,True)
    os.remove(pathsound)

def listen():
    bot = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("F.R.I.D.A.Y: listening...")
        # bot.pause_threshold = 1 #dung 2s roi nghe lenh moi
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


