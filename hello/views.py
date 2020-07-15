from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.templatetags.staticfiles import static
from selenium.webdriver.chrome.options import Options
from threading import Thread

import os
import requests
import time

# Create your views here.
def index(request):
    # create a new Firefox session
    chrome_bin = os.environ.get('GOOGLE_CHROME_SHIM', None)
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.binary_location = chrome_bin
    print(os.path.abspath("chromedriver"))
    driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=chrome_options)
    print("starting web driver")
    driver.get("https://spotery.com/search?psLangId=EN&psAddrCity=San%20Francisco&psSourceFlow=SPOT&psIsGridView=false")
    courts_table = driver.find_element_by_id("pt1:pgl17").get_attribute("innerHTML")
    # windowId = driver.find_element_by_id("f1").get_attribute("innerHTML")
    # print (windowId)
    next_button = driver.find_element_by_id("pt1:lNext::icon")
    next_button.click()
    time.sleep(5);
    second_courts_table = driver.find_element_by_id("pt1:pgl17").get_attribute("innerHTML")
    return HttpResponse(second_courts_table)

    # login_button = driver.find_elements_by_class_name("standalone")[0]
    # login_button.click()
    # # Thread.sleep(1000);
    # username_field = driver.find_element_by_id("username")[0]
    # username_field.send_keys(email)
    # password_field = driver.find_element_by_id("password")[0]
    # password_field.send_keys(password)
    #
    # login_button = driver.find_element_by_css_selector("#login-form .btn")
    # login_button.click()


    # driver.maximize_window()
    #
    # # Navigate to the application home page
    #
    #
    # # get the search textbox
    # search_field = driver.find_element_by_id("lst-ib")
    # search_field.clear()
    #
    # # enter search keyword and submit
    # search_field.send_keys("Selenium WebDriver Interview questions")
    # search_field.submit()
    #
    # # get the list of elements which are displayed after the search
    # # currently on result page using find_elements_by_class_name method
    # lists= driver.find_elements_by_class_name("_Rm")
    #
    # # get the number of elements found
    # print ("Found " + str(len(lists)) + " searches:")
    #
    # # iterate through each element and print the text that is
    # # name of the search
    #
    # i=0
    # for listitem in lists:
    #    print (listitem.get_attribute("innerHTML"))
    #    i=i+1
    #    if(i>10):
    #       break
    #
    # # close the browser window
    # driver.quit()
    #
    # r = requests.get('http://httpbin.org/status/418')
    # print(r.text)
    # return HttpResponse('<pre>' + r.text + '</pre>')
    # return HttpResponse('Hello from Python!')
    # return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
