from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time, random, datetime
import ocr

print(f'''
Program by:
    
 ██████   █████  ███    ██ ██    ██ ███    ███ ███████ ██████  ███████ 
██       ██   ██ ████   ██  ██  ██  ████  ████ ██      ██   ██ ██      
██   ███ ███████ ██ ██  ██   ████   ██ ████ ██ █████   ██   ██ █████   
██    ██ ██   ██ ██  ██ ██    ██    ██  ██  ██ ██      ██   ██ ██      
 ██████  ██   ██ ██   ████    ██    ██      ██ ███████ ██████  ███████ 
                                                                       
''')

chrome_options = Options()
chrome_options.add_argument(
    # outdated '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(options=chrome_options)

accountsToView = ['latimes', 'USERNAME2', 'USERNAME3', 'USERNAME4', 'USERNAME5']  # Enter your usernames here

viewerUsername = 'raitcurmoesg' # Enter the username of the account you wish to view the stories with
viewerPassword = 'raitcurmoesg419'  # Enter your password here


browser.get('https://www.instagram.com/accounts/login/')

time.sleep(random.uniform(1,10.55))

usrname_bar = browser.find_element_by_name('username')  # Find the username bar
passwrd_bar = browser.find_element_by_name('password')  # Find the password bar

print("Logging in as: "+viewerUsername)
usrname_bar.send_keys(viewerUsername)
passwrd_bar.send_keys(viewerPassword + Keys.ENTER)

time.sleep(random.uniform(10.5,11.25))

ocr

for username in accountsToView:

    accountURL = f'https://www.instagram.com/{username}'
    
    browser.get(accountURL)

    time.sleep(random.uniform(1,11.75))

    story_view_btn = browser.find_element_by_class_name('RR-M-.h5uC0')

    story_view_btn.click()

    print("Clicked on Story icon")
    time.sleep(random.uniform(1,20.5))

    print("Viewing "+username+" story.")

    # might not need this if I can take a screenshot: story_image = browser.find_element_by_class_name('y-yJ5 i1HvM')
    URL = browser.current_url
    browser.save_screenshot(f"screenshots/{username}+'-'+{str(datetime.datetime)}+'-'+'.png")
    time.sleep(random.uniform(15,15.5))
    while(URL is not browser.current_url or accountURL):
        print("Waiting for next story chapter")
        URL = browser.current_url
        browser.save_screenshot(f"screenshots/{username}+'-'+{str(datetime.datetime)}+'-'+'.png")
        time.sleep(random.uniform(15,15.5))

    ocr

    print("Saving "+username+" story")
    browser.delete_all_cookies()

    browser.quit()