from selenium.webdriver.common.by import By
from pages.page import Page
from time import sleep

class ROICalculator(Page):
    CalculateMyROIButton = (By.CSS_SELECTOR, "a.cta-button-medium.button-medium_hm-hero.w-button")
    TITLE = (By.CSS_SELECTOR, "div.heading-2.center")
    COOKIESBUTTON = (By.ID, "hs-eu-confirmation-button")
    NUMOFQAGRADERS = (By.ID, "60a5132efd59d92724aa5679")
    NUMOFAGENTS = (By.ID, "60a5132efd59d92724aa5682")
    PERCENTOFCXTEAM = (By.ID, "60a5132efd59d92724aa568b")
    NEXTBUTTON = (By.ID, "60a5132ffd59d92724aa5809")
    FIRSTNAMEFIELD = (By.CSS_SELECTOR, "input.validate.60a5132efd59d92724aa56c10.ng-pristine.ng-valid.valid.ng-touched")
    LASTNAMEFIELD = (By.CSS_SELECTOR, "input.validate.60a5132efd59d92724aa56c11.ng-untouched.ng-pristine.ng-valid")
    EMAILFIELD = (By.ID, "input.validate.60a5132efd59d92724aa56c12.ng-untouched.ng-pristine.ng-valid")
    NUMBEROFTICKETSFIELD = (By.ID, "60a5132efd59d92724aa56b8")
    NUMBEROFMINUTEOFAHT = (By.ID, "60a5132efd59d92724aa56a6")

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.maestroqa.com/cx-quality-assurance-roi-calculator#integrations"

    def open_roicalculator(self):
        self.open_page(self.base_url)

    def cookiesbanner(self):
        sleep(2)
        self.click(*self.COOKIESBUTTON)

    def goto_calculator(self):
        #self.wait_for_element_click(*self.CalculateMyROIButton)
        sleep(2)
        self.click(*self.CalculateMyROIButton)
        sleep(2)

    def find(self, text: str):
        self.verify_text(text, *self.TITLE)

    def click_next_button(self):
        self.click(*self.NEXTBUTTON)

    def fillout_numofgraders_field(self, num):
        sleep(3)
        self.input(num, *self.NUMOFQAGRADERS)

    def fillout_numofagents_field(self, num):
        self.input(num, *self.NUMOFAGENTS)

    def fillout_percents_field(self, num):
        self.input(num, *self.PERCENTOFCXTEAM)

    def fillout_firstName(self, firstName):
        self.input(firstName, *self.FIRSTNAMEFIELD)

    def fillout_lastName(self, lastName):
        self.input(lastName, *self.LASTNAMEFIELD)

    def filloutEmail(self, email):
        self.input(email, *self.EMAILFIELD)

    def filloutNumOfTickets(self, num):
        self.input(num, *self.NUMBEROFTICKETSFIELD)

    def filloutNumOfMinutesOfAHT(self, num):
        self.input(num, *self.NUMBEROFMINUTEOFAHT)

