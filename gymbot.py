from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class GymBot():
    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(chrome_options=options, executable_path='/home/georgejob6/GymBot/chromedriver')

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

    def register(self):
        # 11 am slot, 5 days from now ~ //*[@id="mainContent"]/div[2]/div[7]/div[39]/div/div/div/button //*[@id="mainContent"]/div[2]/div[7]/div[33]/div/div/div/button

        try:
            registerButton = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[49]/div/div/div/button')
            print("Registered for 49th")
        except:
            try:
                registerButton = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[43]/div/div/div/button')
                print("Registered for 43rd")
            except:
                try:
                    registerButton = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[37]/div/div/div/button')
                    print("Registered for 37th")
                except:
                    try:
                        registerButton = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[35]/div/div/div/button')
                        print("Registered for 35th")
                    except:
                        registerButton = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[7]/div[33]/div/div/div/button')

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

    def checkout(self):
        acknowledgeCookiesButton = self.driver.find_element_by_xpath('//*[@id="gdpr-cookie-accept"]')
        acknowledgeCookiesButton.click()

        checkoutButton1 = self.driver.find_element_by_xpath('//*[@id="checkoutButton"]')
        checkoutButton1.click()
        sleep(1)

        checkoutButton2 = self.driver.find_element_by_xpath('//*[@id="ExistingCardsModal"]/div/div/div[2]/div/div[2]/button')
        checkoutButton2.click()


if __name__ == '__main__':
    bot = GymBot()
    bot.login()
    sleep(2)
    bot.register()
    sleep(2)
    bot.checkout()
