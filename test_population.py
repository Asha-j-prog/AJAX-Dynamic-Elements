from selenium import webdriver
from population_page import PopulationPage
import time


def test_world_population():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.worldometers.info/world-population/")

    population = PopulationPage(driver)

    print("\nWorld Population Count:\n")

    # Run only 5 times
    for i in range(5):

        count = population.get_population_count()

        print("Current Population :", count)

        time.sleep(2)

    driver.quit()