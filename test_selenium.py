import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSelenium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def _submit(self, val):
        self.driver.get("http://127.0.0.1:5000")
        if val:
            self.driver.find_element(By.ID, "grades").send_keys(val)
        self.driver.find_element(By.ID, "calculate-btn").click()

    def test_1_moyenne(self): 
        self._submit("12,15,18")
        self.assertIn("15", self.driver.find_element(By.ID, "average").text)

    def test_2_moyenne(self): 
        self._submit("10,10,10")
        self.assertIn("10", self.driver.find_element(By.ID, "average").text)

    def test_3_mention(self): 
        self._submit("8,8,8")
        self.assertIn("Échec", self.driver.find_element(By.ID, "mention").text)

    def test_4_mention(self): 
        self._submit("18,18,18")
        self.assertIn("Excellent", self.driver.find_element(By.ID, "mention").text)

    def test_5_invalide(self): 
        self._submit("12,25,18")
        self.assertTrue(self.driver.find_elements(By.ID, "error-message"))

    def test_6_vide(self): 
        self._submit("")
        self.assertTrue(self.driver.find_elements(By.ID, "error-message"))

if __name__ == "__main__":
    unittest.main()