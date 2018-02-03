import unittest,time,re,os,sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,WebDriverException,NoAlertPresentException

from basetestcase import BaseTestCase
import base_function,booking_functions
from selenium.common.exceptions import NoSuchElementException,WebDriverException
from selenium.webdriver.common.keys import Keys


class Book_small_group(BaseTestCase):


    def test_booking_smallgroupsession(self):
            """
             Test case to verify Booking the small group session
            """
            target = booking_functions.Booking(self.driver)
            BP = base_function.BasePage(self.driver)
            target.search_trainerfor_booking()
            target.dateselect().click()
            target.timeselect().click()
            target.location_field().send_keys(90405)
            target.dropdown_zipocde().click()
            target.classtype_select().click()
            self.driver.implicitly_wait(2)
            target.next_button().is_displayed()
            target.next_button().click()
            target.phone_User().send_keys(1234567890)
            target.small_group().click()
            target.next_button().is_displayed()
            target.next_button().click()
            BP.login_account('testjc88@gmail.com', '8892279018')
            self.driver.implicitly_wait(2)

            target.confirma_paymentbutton().is_displayed()
            target.confirma_paymentbutton().click()
            self.driver.save_screenshot("booked2.png")
            try:
                target.booking_success()

                print(self.driver.find_element_by_css_selector(
                    "#app-layout > section.book-flow > div > div > p").text.strip())
            except:
                print("booking failed due to card was declined")



    def test_cancel_bookings(self):
            """
             Test case to verify Cancel the Booked the session
            """

            target = booking_functions.Booking(self.driver)
            BP = base_function.BasePage(self.driver)
            target.Navigate_workoutscreen()

            try:
                self.accept_next_alert = False
                target.cancel_Appointment().is_displayed()
                target.cancel_Appointment().click()
                self.assertRegexpMatches(self.close_alert_and_get_its_text(),
                                         r"^Are you sure you want to cancel [\s\S]$")
                self.driver.find_element_by_link_text("Cancel Appointment").click()
                self.assertRegexpMatches(self.close_alert_and_get_its_text(),
                                         r"^Are you sure you want to cancel [\s\S]$")
                self.assertEqual("Your booking was deleted!",
                                 self.driver.find_element_by_css_selector("div.alert.alert-success").text)
                print(self.driver.find_element_by_css_selector(
                    "#profile-container > div > div.col-md-10 > div > div > div.alert.alert-success").text)
            except:
                print("Workout section is blank ")


    
    def tearDown(self):
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot(os.getcwd() + '/screenshots/' + test_method_name + "-" + now + ".png")
         # close browser window
        self.driver.quit()


    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True


if __name__ == "__main__":
    unittest.main()