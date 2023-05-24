import webbrowser as wb
import os

def workauto():
    # Path to the code editor executable
    codepath = "E:\\programs\\Microsoft VS Code\\Code.exe"
    
    # Launch the code editor
    os.startfile(codepath)

    # Path to the Google Chrome executable
    Chrome_path = 'C:/Users/hp/AppData/Local/Google/Chrome/Application/chrome.exe %s'

    # List of URLs to be opened in Google Chrome
    URLS = (
        "google.com",
        "gmail.com",
        "github.com/SPrathamesh2611"
    )

    # Open each URL in Google Chrome
    for url in URLS:
        wb.get(Chrome_path).open(url)

# Call the workauto function to initiate the automation
workauto()
