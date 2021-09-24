import os

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegPage import AccountRegPage
from utilities import randomeString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Register:
    #baseURL="https://demo.opencart.com/"
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    @pytest.mark.sanity
    def test_register(self,setup):
        self.logger.info("*** test_001_AccountRegistration started ***")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("*** launching application ***")
    # def test_register(self):
    #     serv_obj = Service("C:/Users/vbobb/Downloads/edge_driver/edgedriver_win64/msedgedriver")
    #     self.driver=webdriver.Edge(service=serv_obj)
    #     self.driver.get("https://demo.opencart.com/index.php?route=account/register")
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.logger.info("*** clicking on MyAccount then Register ***")
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.logger.info("*** Providing the customer details ***")
        self.rp = AccountRegPage(self.driver)
        self.rp.setFirstName("Simon")
        self.rp.setLastName("Antony")
        #self.rp.setEmail("antony1@gmail.com")
        self.email=randomeString.random_string_generator()+'@gmail.com'
        self.rp.setEmail(self.email)
        self.rp.setTelephone("9988776600")
        self.rp.setPassword("antony123")
        self.rp.setPasswordConfirm("antony123")

        #self.rp.clickRDbutton()
        self.rp.clickCheckBox()
        self.rp.clickContinuebutton()
        self.confirmationmsg=self.rp.getconfirmationmsg()

        if self.confirmationmsg=="Your Account Has Been Created!":
            assert True
            self.logger.info("*** test is passed ***")
            self.driver.close()
        else:
            #assert False
             self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_register.png")
             self.logger.error("*** test is failed ***")
             self.driver.close()
             assert False
        self.logger.info("*** test_001_AccountRegistration completed ***")