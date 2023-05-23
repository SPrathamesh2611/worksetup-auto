#work setup automation

import webbrowser as wb
import os

def workauto():
    codepath = "E:\\programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codepath)
    Chrome_path = 'C:/Users/hp/AppData/Local/Google/Chrome/Application/chrome.exe %s'
    URLS = ("google.com",
            "gmail.com",
            "github.com/SPrathamesh2611")
    for url in URLS:
        wb.get(Chrome_path).open(url)

workauto()
