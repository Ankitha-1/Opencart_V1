from selenium.webdriver.common.by import By


class AccountRegPage():
    # Locators
    txt_firstname_id = "input-firstname"
    txt_lastname_id = "input-lastname"
    txt_email_id = "input-email"
    txt_telephone_id = "input-telephone"
    txt_password_id = "input-password"
    txt_passwordconfirm_id = "input-confirm"
    #button_newsletter_xpath = "//*[@id='content']/form/fieldset[3]/div/div/label[2]/input"
    checkbox_privacy_xpath = "// *[ @ id = 'content'] / form / div / div / input[1]"
    button_continue_xpath = "// *[ @ id = 'content'] / form / div / div / input[2]"
    text_msg_confirmation_xpath="//h1[normalize-space()='Your Account Has Been Created!']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # action method
    def setFirstName(self, firstname):
        firstnametxt = self.driver.find_element(By.ID, self.txt_firstname_id).send_keys(firstname)

    def setLastName(self, lastname):
        lastnametxt = self.driver.find_element(By.ID, self.txt_lastname_id).send_keys(lastname)

    def setEmail(self, email):
        emailtxt = self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def setTelephone(self, telephone):
        telephonetxt = self.driver.find_element(By.ID, self.txt_telephone_id).send_keys(telephone)

    def setPassword(self, password):
        passwordtxt = self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def setPasswordConfirm(self, passwordconfirm):
        passwordconfirmtxt = self.driver.find_element(By.ID, self.txt_passwordconfirm_id).send_keys(passwordconfirm)

    # def clickRDbutton(self):
    #     self.driver.find_element(By.XPATH, self.button_newsletter_xpath).click()

    def clickCheckBox(self):
        self.driver.find_element(By.XPATH, self.checkbox_privacy_xpath).click()

    def clickContinuebutton(self):
        self.driver.find_element(By.XPATH, self.button_continue_xpath).click()
    def getconfirmationmsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.text_msg_confirmation_xpath).text
        except:
             None
