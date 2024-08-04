import webbrowser

# webbrowser.open('https://docs.python.org/3.10/library/webbrowser')

# Specifically get the google chrome web browser
# chrome = webbrowser.get(using='google-chrome')
chrome = webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s')

# open a webpage using the browser
chrome.open('https://learnprogramming.academy/courses')