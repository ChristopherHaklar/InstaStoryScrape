# InstaStoryScrape
Scraper and OCR content matching bot for Instagram Stories

# Requirements
- You'll need Chrome installed to allow the script to connect to the Instagram webpage.
- You'll need Tesseract installed from this URL `https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20201127.exe`
- All other Python requirements can be installed by running in your terminal `pip install -r requirements.txt`

# Startup
- To run the script edit the **scrape.py** file to include the username and password of the viewer account, then paste your list of usernames in the `accountsToView` array.
- Then go to **sendAlertEmailWithAttachment.py** and enter your username and password to the gmail account you will use to send the emails.
- Then enter `python scrape.py` in your terminal and hit enter