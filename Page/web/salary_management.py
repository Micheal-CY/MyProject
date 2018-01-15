# -*- coding: utf-8 -*-
import random
import re
from time import sleep
from selenium.webdriver.common.keys import Keys
from Page.Element import get_element, get_elements
from Page.random_data import setting_input_time, getCompanyName
from Page.web.get_now_time import get_now_dates, bug_photo, get_future_date, get_pass_dates
from Page.web.into_level import into_one_level, into_two_level
from Page.web.select_city import select_city, select_city_choice, sub_select_city_choice


def new_payroll(driver, payroll_name):
    into_one_level(driver, '工程面板')
    sleep(1)
    into_two_level(driver, '薪资管理')
    get_element(driver, ('xpath', "//button[@class='btn btn-primary']")).click()
    # 工程名称
    get_element(driver, ('xpath', "//select[@id='kkkk']/option[2]")).click()
    # 输入工资月份
    get_now_dates()
    setting_input_time(driver)
    r = r'\d{4}-\d{2}'
    text = re.findall(r, get_now_dates())
    get_element(driver, ('xpath', "//input[@class='form-control form-n-y-1']")).send_keys(text)
    # 工资单名称
    get_element(driver, ('id', 'createProllNameAll')).clear()
    sleep(0.2)
    get_element(driver, ('id', 'createProllNameAll')).send_keys(payroll_name)
    # 确定按钮
    get_element(driver, ('xpath', "//button[@class='btn btn-primary proll-btn-com']")).click()
    sleep(1)
    get_elements(driver,
                 ('xpath', "//div[@id='createrProll']/div[3]/div[1]/div[2]/div/div[1]/div/div/div/span[2]"))[-1].click()
    sleep(1)
    get_element(driver, ('xpath', "//tr[1]/td[5]/a")).click()
    get_elements(driver, ('xpath', "//input[@class='form-control']"))[1].send_keys()

