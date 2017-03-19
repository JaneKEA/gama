import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class GamaTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\всякие\AppData\Local\Programs\Python\Python36\chromedriver.exe')
        self.driver.implicitly_wait(30)

    def init (self):
        driver = self.driver
        driver.get("http://www.gama-gama.ru/")
        driver.find_element_by_link_text(u"Вход").click()
        driver.find_element_by_name("Email").clear()
        driver.find_element_by_name("Password").clear()

    #check "Есть все необходимые поля"
    def test_gama0(self):
        driver = self.driver
        driver.get("http://www.gama-gama.ru/")
        driver.find_element_by_link_text(u"Вход").click()
        self.assertEqual(u"Необходимо авторизоваться", driver.find_element_by_xpath("//div[@id='authblock']/div").text)
        self.assertEqual("Email:", driver.find_element_by_xpath("//form/div[3]/span").text)
        self.assertEqual("", driver.find_element_by_name("Email").text)
        self.assertEqual(u"Пароль:", driver.find_element_by_xpath("//form/div[4]/span").text)
        self.assertEqual("", driver.find_element_by_name("Password").text)
        self.assertEqual(u"запомнить меня", driver.find_element_by_css_selector("label > span").text)
        self.assertEqual(u"Я не помню пароль", driver.find_element_by_link_text(u"Я не помню пароль").text)
        self.assertEqual(u"Создать аккаунт", driver.find_element_by_link_text(u"Создать аккаунт").text)
        self.assertEqual(u"Войти", driver.find_element_by_xpath("//button").text)
        driver.find_element_by_id("cboxClose").click()

#check "Успешная авторизация"
    def test_gama1(self):
        driver = self.driver
        self.init ()
        driver.find_element_by_name("Email").send_keys("test-gama1@test.com")
        driver.find_element_by_name("Password").send_keys("123")
        driver.find_element_by_xpath("//button").click()
        self.assertEqual(u"Оформляем пропуск…", driver.find_element_by_css_selector("div.status-message").text)
        self.assertEqual(u"Личный кабинет (test-gama1)", driver.find_element_by_link_text(u"Личный кабинет (test-gama1)").text)
        driver.find_element_by_link_text(u"Выход").click()

    # check "Пустые поля"
    def test_gama2(self):
        driver = self.driver
        self.init ()
        driver.find_element_by_xpath("//button").click()
        self.assertEqual(u"Введите E-mail, на который вы регистрировались", driver.find_element_by_css_selector("div.status-error").text)

    #check "Пустой Email"
    def test_gama3(self):
        driver = self.driver
        self. init ()
        driver.find_element_by_name("Password").send_keys("123")
        driver.find_element_by_xpath("//button").click()
        self.assertEqual(u"Введите E-mail, на который вы регистрировались", driver.find_element_by_css_selector("div.status-error").text)

    #check "Пустой пароль"
    def test_gama4(self):
        driver = self.driver
        self.init()
        driver.find_element_by_name("Email").send_keys("test-gama1@test.com")
        driver.find_element_by_xpath("//button").click()
        self.assertEqual(u"Введите ваш пароль", driver.find_element_by_css_selector("div.status-error").text)

    #check "Неправильный пароль"
    def test_gama5(self):
        driver = self.driver
        self.init()
        driver.find_element_by_name("Email").send_keys("test-gama2@test.com")
        driver.find_element_by_name("Password").send_keys("1234")
        driver.find_element_by_xpath("//button").click()
        self.assertEqual(u"Восстановить", driver.find_element_by_link_text(u"Восстановить").text)
        self.assertEqual(u"Неправильный пароль. Восстановить", driver.find_element_by_css_selector("div.status-error").text)

#check "Неправильный логин"
    def test_gama6(self):
        driver = self.driver
        self.init()
        driver.find_element_by_name("Email").send_keys("test-gama1@test.co")
        driver.find_element_by_name("Password").send_keys("123")
        driver.find_element_by_xpath("//button").click()
        self.assertEqual(u"Создать с этим паролем", driver.find_element_by_link_text(u"Создать с этим паролем").text)
        self.assertEqual(u"Такого пользователя не существует. Создать с этим паролем", driver.find_element_by_css_selector("div.status-error").text)

#check "Неправильный логин/пароль"
    def test_gama7(self):
        driver = self.driver
        self.init()
        driver.find_element_by_name("Email").send_keys("test-gama2@test.co")
        driver.find_element_by_name("Password").send_keys("1234")
        driver.find_element_by_xpath("//button").click()
        self.assertEqual(u"Создать с этим паролем", driver.find_element_by_link_text(u"Создать с этим паролем").text)
        self.assertEqual(u"Такого пользователя не существует. Создать с этим паролем", driver.find_element_by_css_selector("div.status-error").text)

 #check "Пробел в логине (до логина)"
    def test_gama8(self):
        driver = self.driver
        self.init()
        driver.find_element_by_name("Email").send_keys("   test-gama2@test.com")
        driver.find_element_by_name("Password").send_keys("123")
        driver.find_element_by_xpath("//button").click()
        self.assertEqual(u"Создать с этим паролем", driver.find_element_by_link_text(u"Создать с этим паролем").text)
        self.assertEqual(u"Такого пользователя не существует. Создать с этим паролем", driver.find_element_by_css_selector("div.status-error").text)

#check "Пробел в логине (после логина)"
    def test_gama9(self):
        driver = self.driver
        self.init()
        driver.find_element_by_name("Email").send_keys("test-gama2@test.com   ")
        driver.find_element_by_name("Password").send_keys("123")
        driver.find_element_by_xpath("//button").click()
        self.assertEqual(u"Создать с этим паролем", driver.find_element_by_link_text(u"Создать с этим паролем").text)
        self.assertEqual(u"Такого пользователя не существует. Создать с этим паролем", driver.find_element_by_css_selector("div.status-error").text)

#check "Регистрозависимость"
    def test_gama10(self):
        driver = self.driver
        self.init ()
        driver.find_element_by_name("Email").send_keys("TEST-GAMA2@TEST.COM")
        driver.find_element_by_name("Password").send_keys("123")
        driver.find_element_by_xpath("//button").click()
        self.assertEqual(u"Оформляем пропуск…", driver.find_element_by_css_selector("div.status-message").text)
        self.assertEqual(u"Личный кабинет (test-gama2)", driver.find_element_by_link_text(u"Личный кабинет (test-gama2)").text)
        driver.find_element_by_link_text(u"Выход").click()

#check "Запомнить меня" - не работает (судя по всему, необходимо дописать установку куков)
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

#check "Я не помню пароль"
    def test_gama12(self):
        driver = self.driver
        self.init ()
        driver.find_element_by_name("Email").send_keys("test-gama3@test.com")
        driver.find_element_by_link_text(u"Я не помню пароль").click()
        self.assertEqual(u"Составляем инструкцию…", driver.find_element_by_css_selector("div.status-message").text)
        try:
            element = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'div.status-message'),u'Инструкция по восстановлению отправлена'))
        except TimeoutException:
            print ('test_gama12 - TimeoutException')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
