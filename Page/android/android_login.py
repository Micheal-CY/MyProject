# -*- coding:utf-8 -*-
# auth:cy
from time import sleep

from Page.Element import get_element, is_element_present
from Page.web.get_now_time import bug_photo


def android_login(driver, username, password):
    try:
        get_element(driver, ('xpath', "//android.widget.EditText[@text='请输入帐号']")).send_keys(username)
        get_element(driver, ('xpath', "//android.widget.EditText[@text='••••••••••']")).send_keys(password)
        get_element(driver, ('ACCESSIBILITY_ID', "登录 ")).click()
        sleep(2)
        assert is_element_present(driver, ('xpath', "//android.view.View[@content-desc='我的']")), '登陆失败'
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False
