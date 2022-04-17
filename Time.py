from datetime import datetime
from Pyaudiovn import Speak_vn
def welcome():
    hour = datetime.now().hour
    if hour<=10:
        Speak_vn("xin chào buổi sáng")
    elif hour<=12:
        Speak_vn("xin chào buổi trưa")
    elif hour<=17:
        Speak_vn("xin chào buổi chiều")
    else:
        Speak_vn("xin chào buổi tối")
    Speak_vn("tôi có thể giúp gì cho bạn")
def time():
    now = datetime.now()
    t = "bây giờ là %d giờ %d phút" %(now.hour,now.minute)
    return t
def date():
    now = datetime.now()
    d = "hôm nay là ngày %d tháng %d năm %d" %(now.day,now.month,now.year)
    return d