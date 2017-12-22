# -*- coding: utf-8 -*-
from time import sleep

from Page.Element import is_element_present, get_element


def handle_permissions_popovers(driver):
    if is_element_present(driver, ('xpath', "//android.widget.TextView[@text='第 1 项权限（共 2 项）']")):
        get_element(driver, ('xpath', "//android.widget.Button[@text='允许']")).click()
        sleep(1)
        if is_element_present(driver, ('xpath', "//android.widget.TextView[@text='第 2 项权限（共 2 项）']")):
            get_element(driver, ('xpath', "//android.widget.Button[@text='允许']")).click()
        else:
            pass
    else:
        pass


