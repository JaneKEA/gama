import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class GamaTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\всякие\AppData\Local\Programs\Python\Python36\chromedriver.exe')
        self.driver.implicitly_wait(30)

##   def test_gama(self):
##        driver = self.driver
##        driver.get("http://www.gama-gama.ru/")
##        driver.find_element_by_link_text(u"Вход").click()
##        driver.switch_to.alert()
##        self.assertEqual(u"Необходимо авторизоваться", driver.find_element_by_xpath("//div[@id='authblock']/div").text)
##        self.assertEqual("Email:", driver.find_element_by_xpath("//form/div[3]/span").text)
##        self.assertEqual("", driver.find_element_by_name("Email").text)
##        self.assertEqual(u"Пароль:", driver.find_element_by_xpath("//form/div[4]/span").text)
##        self.assertEqual("", driver.find_element_by_name("Password").text)
##        self.assertEqual(u"запомнить меня", driver.find_element_by_css_selector("label > span").text)
##        self.assertEqual(u"Я не помню пароль", driver.find_element_by_link_text(u"Я не помню пароль").text)
##        self.assertEqual(u"Создать аккаунт", driver.find_element_by_link_text(u"Создать аккаунт").text)
##        self.assertEqual(u"Войти", driver.find_element_by_xpath("//button").text)
##        driver.find_element_by_id("cboxClose").click()
    def init (self):
        driver = self.driver
        driver.get("http://www.gama-gama.ru/")
        driver.find_element_by_link_text(u"Вход").click()
        driver.find_element_by_name("Email").clear()
        driver.find_element_by_name("Password").clear()

    # def test_gama1(self):
    #     driver = self.driver
    #     self.init ()
    #     driver.find_element_by_name("Email").send_keys("test-gama1@test.com")
    #     driver.find_element_by_name("Password").send_keys("123")
    #     driver.find_element_by_xpath("//button").click()
    #     self.assertEqual(u"Оформляем пропуск…", driver.find_element_by_css_selector("div.status-message").text)
    #     self.assertEqual(u"Личный кабинет (test-gama1)", driver.find_element_by_link_text(u"Личный кабинет (test-gama1)").text)
    #     driver.find_element_by_link_text(u"Выход").click()
    #
    # def test_gama2(self):
    #     driver = self.driver
    #     self.init ()
    #     driver.find_element_by_xpath("//button").click()
    #     self.assertEqual(u"Введите E-mail, на который вы регистрировались", driver.find_element_by_css_selector("div.status-error").text)
    #
    #
    # def test_gama3(self):
    #     driver = self.driver
    #     self. init ()
    #     driver.find_element_by_name("Password").send_keys("123")
    #     driver.find_element_by_xpath("//button").click()
    #     self.assertEqual(u"Введите E-mail, на который вы регистрировались", driver.find_element_by_css_selector("div.status-error").text)
    #
    # def test_gama4(self):
    #     driver = self.driver
    #     self.init()
    #     driver.find_element_by_name("Email").send_keys("test-gama1@test.com")
    #     driver.find_element_by_xpath("//button").click()
    #     self.assertEqual(u"Введите ваш пароль", driver.find_element_by_css_selector("div.status-error").text)
    #
#     def test_gama5(self):
#         driver = self.driver
#         self.init()
#         driver.find_element_by_name("Email").send_keys("test-gama1@test.com")
#         driver.find_element_by_name("Password").send_keys("1234")
#         driver.find_element_by_xpath("//button").click()
#         self.assertEqual(u"Восстановить", driver.find_element_by_link_text(u"Восстановить").text)
#         self.assertEqual(u"Неправильный пароль. Восстановить", driver.find_element_by_css_selector("div.status-error").text)
#
#     def test_gama6(self):
#         driver = self.driver
#         self.init()
#         driver.find_element_by_name("Email").send_keys("test-gama1@test.co")
#         driver.find_element_by_name("Password").send_keys("123")
#         driver.find_element_by_xpath("//button").click()
#         self.assertEqual(u"Создать с этим паролем", driver.find_element_by_link_text(u"Создать с этим паролем").text)
#         self.assertEqual(u"Такого пользователя не существует. Создать с этим паролем", driver.find_element_by_css_selector("div.status-error").text)
#
#
#     def test_gama7(self):
#         driver = self.driver
#         self.init()
#         driver.find_element_by_name("Email").send_keys("test-gama2@test.co")
#         driver.find_element_by_name("Password").send_keys("1234")
#         driver.find_element_by_xpath("//button").click()
#         self.assertEqual(u"Создать с этим паролем", driver.find_element_by_link_text(u"Создать с этим паролем").text)
#         self.assertEqual(u"Такого пользователя не существует. Создать с этим паролем", driver.find_element_by_css_selector("div.status-error").text)
#
#     def test_gama8(self):
#         driver = self.driver
#         self.init()
#         driver.find_element_by_name("Email").send_keys("   test-gama2@test.com")
#         driver.find_element_by_name("Password").send_keys("123")
#         driver.find_element_by_xpath("//button").click()
#         self.assertEqual(u"Создать с этим паролем", driver.find_element_by_link_text(u"Создать с этим паролем").text)
#         self.assertEqual(u"Такого пользователя не существует. Создать с этим паролем", driver.find_element_by_css_selector("div.status-error").text)
#
#
#     def test_gama9(self):
#         driver = self.driver
#         self.init()
#         driver.find_element_by_name("Email").send_keys("test-gama2@test.com   ")
#         driver.find_element_by_name("Password").send_keys("123")
#         driver.find_element_by_xpath("//button").click()
#         self.assertEqual(u"Создать с этим паролем", driver.find_element_by_link_text(u"Создать с этим паролем").text)
#         self.assertEqual(u"Такого пользователя не существует. Создать с этим паролем", driver.find_element_by_css_selector("div.status-error").text)
#
# def test_gama10(self):
#         driver = self.driver
#         self.init ()
#         driver.find_element_by_name("Email").send_keys("TEST-GAMA2@TEST.COM")
#         driver.find_element_by_name("Password").send_keys("123")
#         driver.find_element_by_xpath("//button").click()
#         self.assertEqual(u"Оформляем пропуск…", driver.find_element_by_css_selector("div.status-message").text)
#         self.assertEqual(u"Личный кабинет (test-gama2)", driver.find_element_by_link_text(u"Личный кабинет (test-gama2)").text)
#         driver.find_element_by_link_text(u"Выход").click()

    # def test_gama11(self):
    #     driver = self.driver
    #     self.init ()
    #     driver.find_element_by_name("Email").send_keys("test-gama3@test.com")
    #     driver.find_element_by_name("Password").send_keys("123")
    #     driver.find_element_by_name("StaySignedIn").click()
    #     driver.find_element_by_xpath("//button").click()
    #     self.assertEqual(u"Оформляем пропуск…", driver.find_element_by_css_selector("div.status-message").text)
    #     self.assertEqual(u"Личный кабинет (TEST-GAMA3)", driver.find_element_by_link_text(u"Личный кабинет (TEST-GAMA3)").text)
    #     self.driver.close()
    #     driver.start_session({})
    #     driver.get("http://www.gama-gama.ru/")
    #     self.assertEqual(u"Личный кабинет (TEST-GAMA3)", driver.find_element_by_link_text(u"Личный кабинет (TEST-GAMA3)").text)

    def test_gama12(self):
        driver = self.driver
        self.init ()
        driver.find_element_by_name("Email").send_keys("test-gama3@test.com")
        driver.find_element_by_link_text(u"Я не помню пароль").click()
        self.assertEqual(u"Составляем инструкцию…", driver.find_element_by_css_selector("div.status-message").text)
        element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,'div.status-message'),'test'))
        #self.assertEqual(u"Инструкция по восстановлению отправлена", driver.find_element_by_css_selector("div.status-message").text)

       # elem = driver.find_element_by_name("q")
        #elem.send_keys("pycon")
        #assert "No results found." not in driver.page_source
        #elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
