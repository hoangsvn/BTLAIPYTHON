import wmi,os
from Pyaudiovn import Speak_vn
def Systemcontroler(S):
	S=str(S).lower()
	if "file" in S or "explorer" in S:
		Explorer()
		return False
	elif "cmd" in S or "command line" in S:
		Cmd()
		return False
	elif "info" in S or "systeminfo" in S:
		systemInfo()
		return False
	return True
def systemInfo():
	Speak_vn('Thông tin máy tính')
	c = wmi.WMI()  
	my_system_1 = c.Win32_LogicalDisk()[0]
	my_system_2 = c.Win32_ComputerSystem()[0]
	info = ["Total Disk C: Space: " + str(round(int(my_system_1.Size)/(1024**3),2)) + " GB",
			"Free Disk C: Space: " + str(round(int(my_system_1.Freespace)/(1024**3),2)) + " GB",
			"Manufacturer: " + my_system_2.Manufacturer,
			"Model: " + my_system_2. Model,
			"Owner: " + my_system_2.PrimaryOwnerName,
			"Number of Processors: " + str(my_system_2.NumberOfProcessors),
			"System Type: " + my_system_2.SystemType]
	string=''
	for s in info:
		string=f'{string} {s}\n'
	print (string)

def Explorer():
	Speak_vn('Đang mở File Explorer')
	os.startfile('C:\Windows\explorer.exe')
def Cmd():
	Speak_vn('Đang mở Command Line')
	os.startfile('C:\Windows\System32\cmd.exe')
if __name__=='__main__':
	Explorer()
	Cmd()