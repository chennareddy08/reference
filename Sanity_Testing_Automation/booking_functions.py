# -*- coding: utf-8 -*-
import unittest,time
from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date, timedelta
from selenium.webdriver.common.action_chains import ActionChains
from base_function import BasePage

from selenium.common.exceptions import NoSuchElementException,WebDriverException





class Booking(object):
    """ All page objects inherit from this """


    def __init__(self,driver):
        self.driver  = driver
        self.wait = WebDriverWait(self.driver, 15)


    def findTrainer_button(self):
        """Function Verify find trainer buttin is visible"""
        self.wait = WebDriverWait(self.driver, 15)
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app-layout > section.hero > div > div > div > div.hero-search > form > div > span > button")));


    def zipcode_field(self):
        """Function Verify zipcode field is visible"""
        self.wait = WebDriverWait(self.driver, 15)
        return self.wait.until(EC.element_to_be_clickable((By.ID,'home-zip-code')))

    def passportadd(self):
        self.wait = WebDriverWait(self.driver, 30)
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#passport-ad > div.box")))

    def select_trainer(self):
        """Function Verify trainer list  is visible"""
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='1887']/a/div[1]/img")))

    def trainer_passport_selection(self):
        """Function Verify try passport is visible"""
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Try Passport")))

    def handstandchoicelist(self):
        """Function Verify thandstandchoice list is visible"""
        #self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.box > div:nth-of-type(1) > a > div.thumb-nail > img"))
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.box > div:nth-of-type(1) > a > div.thumb-nail > img")))

    def Book_button_trainers(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.jscroll-inner > div:nth-of-type(1) > div.box > div.caption > div.trainer-button > div.cta-traininglist > a > div.cta")))

    def phone_User(self):
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(EC.element_to_be_clickable((By.NAME,"phone")))


    def HomeTab(self):
        """Function Verify Home Tab is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Home")))

    def ApplyToTrainerTab(self):
        """Function Verify Home Tab is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Apply to be a trainer")))


    def booking_button(self):

        """Function Verify BookingButton is visible"""
        self.wait = WebDriverWait(self.driver,10)
        return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Book")))

    def searchbutton(self):
        """Function Verify search icon is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"ui-button block trainers-filters-submit-button")))

    # def booking_button(self):
    #     return self.wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='1742']/a/div")))


    def clearsearch(self):
        """Function Verify clearsearch is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#clear-search")))

    def closebutton_bookingpage(self):
        """Function Verify closebutton on bookingpageis visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-details > div.box > div.close")))

    def closebutton_datepage(self):
         """Function Verify closebutton on datepage is visible"""
         return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-when > div.box > div.close")))

    def closebutton_timepage(self):
         """Function Verify closebutton on time page is visible"""
         return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#trainer-time > div.box > div.close")))

    def closebutton_classtypeepage(self):
         """Function Verify closebutton on classtype page is visible"""
         return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#trainer-class > div.box > div.close")))

    def closebutton_locationpage(self):
         """Function Verify closebutton on location page page is visible"""
         return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#trainer-location > div.box > div.close")))

    def closebutton_reviewpage(self):
         """Function Verify closebutton on review page page is visible"""
         return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#trainer-review > div.box > div.close")))

    def forward_arrowbutton_bookingpage(self):
        """Function Verify forward arrowbutton on bookingpage is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-details > div.box > div.trainer-nav.forward")))

    def forward_arrowbutton_datepage(self):
        """Function Verify forward arrowbutton on datepage is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-when > div.box > div.trainer-nav.forward")))

    def forward_arrowbutton_timepage(self):
        """Function Verify forward arrowbutton on time page is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR," #trainer-time > div.box > div.trainer-nav.forward")))


    def forward_arrowbutton_locationpage(self):
        """Function Verify forward arrowbutton on location page is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-location > div > div.trainer-nav.forward")))

    def forward_arrowbutton_classtypepage(self):
        """Function Verify forward arrowbutton on class type page is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-class > div.box > div.trainer-nav.forward")))


    def backwardarrowbutton_datepage(self):
        """Function Verify fbackward arrowbutton on datepage is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-when > div.box > div.trainer-nav.back")))


    def backwardarrowbutton_timepage(self):
        """Function Verify fbackward arrowbutton on datepage is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-time > div.box > div.trainer-nav.back")))

    def backwardarrowbutton_locationpage(self):
        """Function Verify backward arrowbutton on location page is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-location > div > div.trainer-nav.back")))

    def backwardarrowbutton_classtypepage(self):
        """Function Verify backward arrowbutton on class type page is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-class > div.box > div.trainer-nav.back")))

    def backwardarrowbutton_reviewpage(self):
        """Function Verify backward arrowbutton on review page is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#trainer-review > div.box > div.trainer-nav.back")))

    def location_field(self):
         """Function Verify  on location field page is visible"""
         return self.wait.until(EC.element_to_be_clickable((By.ID,"bookLocation")))

    def locationdropdownsearch(self):
        """Function Verify  on location drop down search list is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[1]/div[1]")))

    def one_on_oneselection(self):
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(EC.element_to_be_clickable((By.ID, "size1")))


    def small_group(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID,"size2")))


    def promo_field(self):
        """Function Verify  on promo field page is visible"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#promo")))

    def click_book_nowbutton(self):
        """Function Verify  on click on book now is visible"""
        return self.wait.until((EC.element_to_be_clickable((By.CSS_SELECTOR,"#bookBtn"))))

    def next_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#app-layout > section.book-flow > div > form > div > div.book-panel-footer.panel-footer > button")))


    def confirma_paymentbutton(self):
        """Function Verify   button is visible"""
        return self.wait.until((EC.element_to_be_clickable((By.ID,"submit-button"))))

    def individual_checbox(self):
        """Function Verify  on individual checkbox is visible"""
        return self.wait.until((EC.element_to_be_clickable((By.ID,"individual"))))


    def profileimage(self):
        """
        Function Verify  on profile image is visible
        """
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='profile-pic']/img")))



    def profiletab(self):

        """
        Function Verify  on profile tab is visible
        """
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='profile-dropdown']/ul/a[1]/li")))


    def workouttab(self):
        """
        Function Verify  on workout tab is visible
        """
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='profile-nav']/ul/a[1]/li")))


    def cancel_Appointment(self):
        """
        Function Verify  on cancel button is visible on workout section
        """
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#profile-container > div > div.col-md-10 > div > div > div > div > div > div > div > div.col-md-10 > div > div:nth-child(3) > a")))




   
    def dateselect(self):
        """function to select date"""
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(EC.element_to_be_clickable((By.ID, "date-4")))

    def timeselect(self):
        """function to select time"""
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#day-times-4 > div > div > div:nth-child(7) > label")))

    def classtype_select(self):
        """function to select class type"""
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#app-layout > section.book-flow > div > form > div > div.panel-body > div.book-form > div > div > div:nth-child(1) > label")))

    def dropdown_zipocde(self):
        """function to select dropdown_zipocde"""
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[1]/div[1]")))


    def leavemsg_widget(self):
        """Function Verify leavemsg widget is visisble """
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.meshim_widget_widgets_BorderOverlay")))

    def booking_success(self):
        return self.driver.find_element_by_css_selector("#app-layout > section.book-flow > div > div")



    # def date_select(self):
    #     datelist = self.driver.find_elements_by_xpath("html/body/section[1]/div/form/div/div[2]/div[2]/div/div/div/div")
    #     print('Total no of dates available for booking are', len(datelist))
    #     for i in range(1, len(datelist)):
    #             print('The user selected date is', datelist[i].text)
    #             try:
    #                 while(datelist[i+1].is_enabled()):
    #                     datelist[i].click()
    #             except:    pass
    #
    # def timeselect(self):
    #     timelist = self.driver.find_elements_by_xpath("html/body/section[1]/div/form/div/div[2]/div[3]/div[5]/div/div/div")
    #     for i in range(1, len(timelist)):
    #         try:
    #             if timelist[i].is_enabled():
    #                 timelist[i].click()
    #                 break
    #             else:
    #                     Booking.dateselect().click()
    #                     timelist[i].click()
    #         except:pass






            # Booking.location_field().send_keys(90405)
            # Booking.dropdown_zipocde().click()
            # Booking.classtype_select().click()
            # self.driver.implicitly_wait(2)
            # Booking.next_button().is_displayed()
            # Booking.next_button().click()



    def search_trainerfor_booking(self):
        """
            Test case to verify Book a Workout page
           """
        self.driver.set_window_size(1250, 1024)
        Booking.zipcode_field(self).clear()
        Booking.zipcode_field(self).send_keys(90405)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

        self.driver.implicitly_wait(2)
        self.driver.find_element_by_name("query").send_keys("Handstand5")

        self.driver.find_element_by_css_selector(".ui-button.block.trainers-filters-submit-button").click()
        self.driver.implicitly_wait(2)
        try:
            self.driver.find_element_by_link_text("Book").is_displayed()
            self.driver.find_element_by_link_text("Book").click()
            self.driver.implicitly_wait(2)
        except:
            print('trainer time slot is not available in this schedule,please select another time slot')

    def login_account(self, email, password):
        """function use to login account"""
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-footer > button").click()



    def Navigate_workoutscreen(self):
        """function to Navigate to Workout screen"""

        self.driver.find_element_by_link_text('Login').click()
        self.driver.find_element_by_id('email').send_keys("testjc88@gmail.com")
        self.driver.find_element_by_id('password').send_keys(8892279018)
        self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-footer > button").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id("base-nav-link-toggle").click()

        self.driver.find_element_by_link_text("Settings").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_link_text("My Upcoming Workouts").click()



    def Navigate_TrainerprofileScreen(self,username,password):
        """function to Navigate to Workout screen"""

        self.driver.find_element_by_link_text('Login').click()
        self.driver.find_element_by_id('email').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_css_selector("#app-layout > div > form > div > div.panel-footer > button").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id("base-nav-link-toggle").click()

        self.driver.find_element_by_link_text("Settings").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_link_text("Trainer Profile").click()
        assert self.driver.find_element_by_css_selector('#profile-container > div > div.col-md-10 > div > div > h3').text == 'Profile Information'



    def zipcode_entry(self,zipcode):
        """Function Verify zipcode entry and navigate to trainer list screen """
        Booking.zipcode_field(self).clear()
        Booking.zipcode_field(self).send_keys(zipcode)
        Booking.findTrainer_button(self).click()




    def login_slackVerify(self,email,password):

        self.driver.get("https://scienceinc.slack.com/messages/handstandapp/")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("signin_btn").click()
        self.driver.implicitly_wait(40)


    def booking_cleanup(self):
        BasePage.login_gmail(self,'handstandtest3@gmail.com','7259692024')
        self.driver.implicitly_wait(10)
        try:
            while self.driver.find_element_by_xpath("//div[@class='y6']/span[contains(.,'HandStand Booking Confirmation')]").text=="HandStand Booking Confirmation":
                self.driver.find_element_by_xpath("//div[@id=':3f']/div").click()
                self.driver.implicitly_wait(5)
                BasePage.gmail_logouttabdisplay(self).click()
        except NoSuchElementException:
             self.driver.find_element_by_css_selector("span.gb_Za.gbii").click()
             self.driver.find_element_by_id("gb_71").click()


    def promocode_entry_reviewpage(self,promo):
        """Function to Verify promo entry  """
        Booking.promo_field(self).clear()
        Booking.promo_field(self).send_keys(promo)

    def verify_sessionbooked_confirmation(self):
        """Function to Verify booking confirmation pop up msg  """

        self.assertTrue(self.is_element_present(By.XPATH, ".//*[@id='trainer-booked']"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#trainer-booked > div > header > h5"))
        self.driver.save_screenshot("booked1.png")
#        assert "Session Booked"==self.driver.find_element_by_css_selector("#trainer-booked > div > header > h5").text
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, " #final-review"))
        assert "Done"==self.driver.find_element_by_link_text("Done").text


















    def verify_cancelworkoutpage_confirmation(self):
        assert 'Cancel Workout' == self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("#workout-cancel > div.box > header > h5"))
        e3=self.driver.find_element_by_css_selector("form > div.details")
        print(self.driver.execute_script("return arguments[0].textContent",e3))
        #assert "Are you sure you want to cancel this workout ?"== self.driver.execute_script("return arguments[0].textContent",e3)

    def verify_workoutblocked_popup(self):
        assert 'Workout Blocked'==self.driver.execute_script("return arguments[0].textContent",self.driver.find_element_by_css_selector("#workout-cancel > div.box > header > h5"))


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True


class InvalidPageException(Exception):
    """ Throw this exception when you don't find the correct page """
    pass
