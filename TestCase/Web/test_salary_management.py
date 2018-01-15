# -*- coding: utf-8 -*-
# auth:CY
import unittest
from configparser import ConfigParser
from selenium import webdriver as browse_driver

from Page.random_data import getPeopleName
from Page.web.logout import logout
from Page.web.salary_management import new_payroll
from Page.web.web_login import web_login
from run_path import setting_path


class SalaryManagement(unittest.TestCase):
    def setUp(self):
        config = ConfigParser()
        config.read(setting_path())
        self.driver = browse_driver.Firefox()
        self.driver.maximize_window()
        self.driver.get(config.get('testUrl', 'url'))
        self.username = config.get('labor', 'Wuhuigang')
        self.password = config.get('operation', 'password')
        self.payroll_name = getPeopleName()

    def tearDown(self):
        self.driver.close()

    def test_01_login(self):
        web_login(self.driver, self.username, self.password)
        new_payroll(self.driver, self.payroll_name)



