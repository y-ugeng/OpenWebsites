import webbrowser

#ff_path = "C:\Program Files\Mozilla Firefox\firefox.exe"
webbrowser.register('firefox', None, webbrowser.GenericBrowser('firefox'))
browser = input("Enter browser to use: ")
url = input("Enter website: ")
tabs = int(input("Enter number of tabs to open: "))
count = 0

if (browser == "google chrome" or browser == "chrome"):
	while count < tabs:
		webbrowser.open(url)
		count += 1

elif browser == "firefox" :
	while count < tabs:
		webbrowser.get('firefox').open(url)
		count += 1
