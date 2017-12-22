# -*- coding: utf-8 -*-
# auth:CY
import unittest
from configparser import ConfigParser
from time import sleep
from appium import webdriver
from Page.android.android_login import android_login
from Page.android.android_registration import workers_registration
from Page.android.get_udid import get_android_udid, get_android_version, android_7_uninstall
from Page.android.handle_permissions_popovers import handle_permissions_popovers
from Page.android.start_appium import start_android_appium
from Page.android.stop_appium import stop_android_appium
from Page.random_data import get_mobile
from run_path import setting_path


class Android_login(unittest.TestCase):
    def setUp(self):
        config = ConfigParser()
        config.read(setting_path())
        self.username = config.get('operation', 'username')
        self.password = config.get('operation', 'password')
        self.mobile = get_mobile()
        device_name = get_android_udid()
        stop_android_appium()
        sleep(2)
        start_android_appium(device_name)
        desired_caps = {
            'platformName': 'Android',
            'deviceName': device_name,
            'platformVersion': get_android_version(),
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'appPackage': 'cn.zlddata.zldtest',
            'appActivity': 'cn.zlddata.zldtest.MainActivity',

        }

        if get_android_version()[:3] == '7.0':
            android_7_uninstall()
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(6)
        handle_permissions_popovers(self.driver)

    def tearDown(self):
        self.driver.quit()
        stop_android_appium()

    def test_01_login(self):
        android_login(self.driver, self.username, self.password)

    def test_02_registration(self):
        workers_registration(self.driver, self.mobile, self.password)
        pass

