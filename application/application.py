from pages.page import Page
from pages.ROICalculator import ROICalculator


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.page = Page(self.driver)
        self.ROICalculator = ROICalculator(self.driver)


