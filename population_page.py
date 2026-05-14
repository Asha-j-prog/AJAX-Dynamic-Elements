from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PopulationPage:

    def __init__(self, driver):

        self.driver = driver

    # XPATH only
    population_xpath = "//span[@rel='current_population']"

    def get_population_count(self):

        population = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, self.population_xpath)
            )
        )

        return population.text