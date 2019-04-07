

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class SkyNewsMain:
    driver = webdriver.Chrome("chromedriver.exe")
    pagetitle = ' '

    def __init__(self):
        pass
    
    def __del__(self):
        self.driver.close()

    @classmethod
    def launch_browser(self):
        self.driver.get('https://news.sky.com/')
        accept_button = self.driver.find_element_by_xpath("//button[contains(.,'Accept')]")
        accept_button.send_keys(Keys.RETURN)
        time.sleep(2)

    def check_browser_title(self):
        self.pagetitle = self.driver.title
        return True

    def verify_returned_title(self):
        expected_title = "The Latest News from the UK and Around the World | Sky News"
        if expected_title == self.pagetitle:
            return True
    
    def check_categories(self):
        expected = ['Home', 'UK', 'World', 'Politics', 'US', 'Ocean Rescue', 'Science & Tech']
        xpath = "//div[@id='nav-wrap']//ul[@class='sdc-site-header__menu-cell sdc-site-header__menu-cell--1']"
        categories = self.driver.find_element_by_xpath(xpath).text.split('\n')
        if (expected == categories):
            return True
        else:
            return False

    def check_home_categories(self):
        expected = 'Home'
        xpath = "//div[@id='nav-wrap']//ul[@class='sdc-site-header__menu-cell sdc-site-header__menu-cell--1']//li"
        result = self.driver.find_element_by_xpath(xpath).text
        if (expected == result):
            return True
        else:
            return False

    def click_ocean_rescue(self):
        xpath ="//div[@id='nav-wrap']//ul[@class='sdc-site-header__menu-cell sdc-site-header__menu-cell--1']//li//a[contains(text(),'Ocean Rescue')]"
        OceanRescue = self.driver.find_element_by_xpath(xpath)
        OceanRescue.click()

    def check_header_text(self):
        time.sleep(3)
        expected = 'Ocean Rescue'
        xpath ="//div[@id='nav-wrap']//ul[@class='sdc-site-header__menu-cell sdc-site-header__menu-cell--1']//li//a[@aria-current='true']"
        result = self.driver.find_element_by_xpath(xpath).text
        print(result)
        if (expected == result):
            return True
        else:
            return False