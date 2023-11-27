from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


textForMail = []

gmail = "" #my school gmal
username = "" #username to school site
password = "" #password to school site

driver1 = webdriver.Chrome(executable_path="C:\Program Files\chromedriver", options = options)

driver1.get("") #school website


sleep(3)

gmailInput = driver1.find_element("xpath",'//*[@id="Username"]')
gmailsubmit = driver1.find_element("xpath", '//*[@id="nextBtn"]')

gmailInput.send_keys(gmail)
sleep(.5)
gmailsubmit.click()
sleep(5)

usernameInput = driver1.find_element(By.XPATH, '//*[@id="okta-signin-username"]')
passwordInput = driver1.find_element("xpath", '//*[@id="okta-signin-password"]')
user_passSubmit = driver1.find_element("xpath", '//*[@id="okta-signin-submit"]')

usernameInput.send_keys(username)
sleep(.1)
passwordInput.send_keys(password)
sleep(.5)
user_passSubmit.click()

sleep(15)

showButton = driver1.find_element("xpath", '//*[@id="showHideGrade"]/div/label[1]')

showButton.click()

sleep(1)

#start scarping the grades

grades = driver1.find_elements(By.CLASS_NAME, "showGrade")

for i in range(len(grades)):
    theClass = driver1.find_element(By.XPATH, '//*[@id="coursesContainer"]/div['+str(i+1)+']/div[1]/a/h3')
    textForMail.append(theClass.text)
    textForMail.append(grades[i].text)
    textForMail.append('\n')

textForMail = ' '.join(textForMail)

print(textForMail)

#GMAIL-Text to me

from email.message import EmailMessage
import smtplib
import email


email_sender = ''#my email sending it from
email_password = ''#verification password for that email
email_recevers = [] #list of phonenumbers to send it to using free sms gateway from service provider

for email_recever in email_recevers:
    subject = "    Brady's Grades"
    body = textForMail

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_recever
    em['Subject'] = subject
    em.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_recever, em.as_string())

    print("done")