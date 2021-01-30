from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class GymBot():

    # initialize an instance of Chrome for the webdriver to work with
    # operating in headless mode 
    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(chrome_options=options, executable_path='/home/georgejob6/GymBot/chromedriver')

    # logs into the website using the top right login button
    # locates username and password field and fills in corresponding values
    # locates login button and clicks to login
    def login(self):
        self.driver.get('https://services.rec.rutgers.edu/Program/GetProgramDetails?courseId=694b3079-a4f9-4988-94d5-6374f9d3fe40&semesterId=61d7fedd-4078-466e-afda-7003ce3123ac')
        loginButton = self.driver.find_element_by_xpath('//*[@id="loginLink"]')
        loginButton.click()
        sleep(1)

        netIDButton = self.driver.find_element_by_xpath('//*[@id="divLoginOptions"]/div[2]/div[2]/div/button')
        netIDButton.click()
        sleep(1)

        netIDUsername = self.driver.find_element_by_xpath('//*[@id="username"]')
        netIDUsername.send_keys('*****')

        netIDpw = self.driver.find_element_by_xpath('//*[@id="password"]')
        netIDpw.send_keys('*****')

        netIDLogin = self.driver.find_element_by_xpath('//*[@id="fm1"]/section/input[4]')
        netIDLogin.click()

    # Selects the 11AM - 12:30PM time slot 5 days from the current date to register for
    # Some time slots five days from now will have different xpaths due to different number of time slots offered on weekends
    # Answers the 6 question questionaire on the following page and then adds to cart
    def register(self):
        # 11 am slot, 5 days from now ~ 59th card(Sat), 51st card(Fri,Sun), 43rd card(Mon,Tues,Wed,Thurs)

        try:
            registerButton = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[59]/div/div/div/button')
            print("Registering for 59th card")
        except:
            try:
                registerButton = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[51]/div/div/div/button')
                print("Registering for 51st card")
            except:
                try:
                    registerButton = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[43]/div/div/div/button')
                    print("Registering for 43rd card")
                except:
                    print("Unable to find card...")
                            

        registerButton.click()
        sleep(2)

        q1 = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/form[2]/div[1]/div[1]/div/div[2]/div/div/label[1]')
        q2 = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/form[2]/div[1]/div[2]/div/div[2]/div/div/label[1]')
        q3 = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/form[2]/div[1]/div[3]/div/div[2]/div/div/label[1]')
        q4 = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/form[2]/div[1]/div[4]/div/div[2]/div/div/label[1]')
        q5 = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/form[2]/div[1]/div[5]/div/div[2]/div/div/label[1]')
        q6 = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/form[2]/div[1]/div[6]/div/div[2]/div/div/label[1]')

        q1.click()
        q2.click()
        q3.click()
        q4.click()
        q5.click()
        q6.click()

        addToCartButton = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/form[2]/div[2]/button[2]')
        addToCartButton.click()

    # Confirms the registration on the final checkout page
    def checkout(self):
        acknowledgeCookiesButton = self.driver.find_element_by_xpath('//*[@id="gdpr-cookie-accept"]')
        acknowledgeCookiesButton.click()

        checkoutButton1 = self.driver.find_element_by_xpath('//*[@id="checkoutButton"]')
        checkoutButton1.click()
        sleep(1)

        checkoutButton2 = self.driver.find_element_by_xpath('//*[@id="ExistingCardsModal"]/div/div/div[2]/div/div[2]/button')
        checkoutButton2.click()
        sleep(1)



if __name__ == '__main__':
    bot = GymBot()

    try:
        bot.login()
        sleep(2)
        bot.register()
        sleep(2)
        bot.checkout()
    finally:
        bot.driver.quit()