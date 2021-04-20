from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time, random, datetime

usrnames = ['b31ngd3v']  # Account on which You want to send views

chrome_options = Options()
chrome_options.add_argument(
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
browser = webdriver.Chrome(options=chrome_options)

accountsToView = ['USERNAME1', 'USERNAME2', 'USERNAME3', 'USERNAME4', 'USERNAME5']  # Enter your usernames here
viewerUsername = 'raitcurmoesg'
viewerPassword = 'raitcurmoesg419'  # Enter your password here


browser.get('https://www.instagram.com/accounts/login/')

time.sleep(random.random(1,10.55))

usrname_bar = browser.find_element_by_name('username')  # Find the username bar
passwrd_bar = browser.find_element_by_name('password')  # Find the password bar

print("Logging in as: "+viewerUsername)
usrname_bar.send_keys(viewerUsername)
passwrd_bar.send_keys(viewerPassword + Keys.ENTER)

time.sleep(11)

for usernames in accountsToView:

    browser.get(f'https://www.instagram.com/{usernames}')

    time.sleep(random.random(1,11.75))

    story_view_btn = browser.find_element_by_class_name('_2dbep')

    story_view_btn.click()

    time.sleep(random.random(1,20.5))

    print("Viewing "+usernames+" story.")

    # might not need this if I can take a screenshot: story_image = browser.find_element_by_class_name('y-yJ5 i1HvM')

    browser.save_screenshot(usernames+str(datetime.datetime)+".png")
    browser.execute_script("return document.documentElement.outerHTML")


    print("Saving "+usernames+" story")
browser.delete_all_cookies()

browser.quit()

print(f'''
Program by:
    
 ██████   █████  ███    ██ ██    ██ ███    ███ ███████ ██████  ███████ 
██       ██   ██ ████   ██  ██  ██  ████  ████ ██      ██   ██ ██      
██   ███ ███████ ██ ██  ██   ████   ██ ████ ██ █████   ██   ██ █████   
██    ██ ██   ██ ██  ██ ██    ██    ██  ██  ██ ██      ██   ██ ██      
 ██████  ██   ██ ██   ████    ██    ██      ██ ███████ ██████  ███████ 
                                                                       
''')