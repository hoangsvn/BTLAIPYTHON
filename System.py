import wmi
from Pyaudiovn import Speak_vn
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
if __name__=='__main__':
	systemInfo()