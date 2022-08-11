
# scraper for the following website:
# selenium webdriver
# https://oldschool.runescape.com/
import time
from webbrowser import Chrome

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import geckodriver_autoinstaller
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

profile = webdriver.FirefoxProfile()


# with authentication and socks5 proxy
def getProxyDriver():
    # create a new instance of the chrome driver
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.socks", '127.0.0.1')
    profile.set_preference("network.proxy.socks_port", 9150)
    profile.set_preference("network.proxy.socks_remote_dns", False)
    profile.update_preferences()
    return webdriver.Firefox(firefox_profile=profile)


class Scraper:
    def __init__(self, debug):
        self.driver = getProxyDriver()
        self.driver.get("https://oldschool.runescape.com/")
        self.driver.implicitly_wait(10)
        self.acceptCookiesIfAsked()

    def connect(self, username, password):
        self.driver.find_element(By.ID, "showOsLogin").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "os-login-submit").click()
        self.driver.implicitly_wait(10)
        input("Press Enter to continue...")

    def acceptCookiesIfAsked(self):
        try:
            self.driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
            print("accepted cookies")
            self.driver.implicitly_wait(10)
        except:
            print("no cookies")
            pass


Scraper(True).connect("spilsebbe@live.dk", "120602")
Scraper(True).connect("furiiibond@gmail.com", "jcl00000000")
Scraper(True).connect("salty@grind.rs", "nka83kfv")
