#Github link: https://github.com/JewsOfHazard/RenameUningineHeavenBenchmark
import os

def setScriptLocation():
	os.chdir(os.path.dirname(os.path.realpath(__file__)))

def getMonth(month):
	return {
		'01':'Jan',
		'02':'Feb',
		'03':'March',
		'04':'April',
		'05':'May',
		'06':'June',
		'07':'July',
		'08':'Aug',
		'09':'Sep',
		'10':'Oct',
		'11':'Nov',
		'12':'Dec'
	}[month]
	
def getDate(date):
	dict = {
		'01':'st',
		'02':'nd',
		'03':'rd'
	}
	return date + dict.get(date, 'th')
	
def getTime(time):
	if int(time) < 1200:
		return time+"AM"
	else:
		formatted_time = str(int(time)-1200)+"PM"
		if len(formatted_time) == 4:
			return "12"+formatted_time
		elif len(formatted_time) == 5:
			return "0"+formatted_time
		else:
			return formatted_time

if __name__ == "__main__":
	setScriptLocation()
	
	for file in os.listdir(os.getcwd()):
		if file not in os.path.basename(__file__) and len(file) is 47:
			os.rename(file, file[:29]+getMonth(file[33:35])+"-"+getDate(file[35:37])+"-"+file[29:33]+"-"+getTime(file[38:42])+".html")
			