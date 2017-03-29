# -*- coding: utf-8 -*-

from __future__ import unicode_literals


page_objects_dict = {

    #  LOGIN PAGE
    'login_username_field': '//input[@id="id_username"]',
    'login_password_field': '//input[@id="id_password"]',
    'login_button': '//button[@id="login_button"]',

    #  MAIN MENU
    'main_page': '//a[@id="main_menu"]',
    'foo': '//a[@id="foo"]',
    'new_user': '//a[@id="new_user"]',
    'logs': '//a[@id="logs"]',
    'logged_user': '//*[@id="logged_user"]',

    #  NEW USER
    'new_user_username': '//input[@id="id_username"]',
    'new_user_password': '//input[@id="id_password"]',
    'new_user_is_admin': '//input[@id="id_is_staff"]',
    'new_user_location': '//input[@id="id_location"]',
    'new_user_submit': '//input[@id="new_user_submit"]',
    'phone_number': '//input[@id="id_phone_number"]',
    'phone_number2': '//input[@id="id_phone_number2"]',
    'phone_number3': '//input[@id="id_phone_number3"]',

    #  LOGS
    'search_box': '//input[@id="searchbox"]',
    'search_button': '//button[@id="search_button"]',
    'clear_button': '//a[@id="clear_data"]',
    'log_table': '//table[@id="log_table"]',
    'last_log_time': '//table[@id="log_table"]/tbody/tr[2]/td[3]',

    #  USER PAGE
    'logout_button': '//*[@id="logout_button"]',

}
