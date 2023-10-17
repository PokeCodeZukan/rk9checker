from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import webbrowser
import os
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    # Set up your email server and credentials
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "smtp@gmail.com" #Add your email here"
    smtp_password = "qwer tyui opas dfgh" #your app password
    from_address = "from@gmail.com" #add from address, usually your smtp address
    to_addresses = ["fasfdasf@gmail.com"
                    , "asdfafd@hotmail.com", 
                    "asdfa.fdg.90@gmail.com"
                    ]  #recipients

    #create  email
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_address
    msg["To"] = ", ".join(to_addresses)  # join emails with commas

    #smtp
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(from_address, to_addresses, msg.as_string())  
    server.quit()


#options
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\\Users\\franc\\AppData\\Local\\Google\\Chrome\\User Data") #add your chrome profile path
chrome_options.add_argument("--profile-directory=Default") #usually default but change to profile already logged to the site

#webdriver
driver = webdriver.Chrome(options=chrome_options)

#la url
url = 'https://rk9.gg/register/LA1KwuOf7o9YjRkA9dlBFO8' #change to the site you want to explore message
driver.get(url)

# Wait for the login page to load
time.sleep(10)  # Adjust this wait time as necessary

# At this point, you would manually log in using the browser window that Selenium opened.
# Once logged in, you can uncomment the following lines to check the page content:
# Note: lines below are actually uncommented, given if you already set up profile logged in to site, othwerwise, 1-.comment out 2-run first time , login 3-uncomment

# Check the page content
page_content = driver.page_source

# with open('page_content.html', 'w', encoding='utf-8') as file:
#     file.write(page_content) #check full site content and show in screen

# Open the saved page content in the default web browser
# webbrowser.open('file:///' + os.path.abspath('page_content.html'))

while True:
    driver.refresh()  # Refresh the page
    time.sleep(10)  # Wait 10 seconds before checking the page content
    page_content = driver.page_source
    if "We're sorry, the tournament has reached maximum capacity for your division (Masters)," \
       " so you are not able to register." not in page_content: #change to whatever meessage you want to check in the given site
        send_email("RK9 Inter Registro", "Deberia estar abierto el registro! https://rk9.gg/register/LA1KwuOf7o9YjRkA9dlBFO8") #change (subject, content) to whatever you like
        break  # Exit the loop if the message is not found

# Close the WebDriver instance
driver.quit()