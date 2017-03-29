# -*- coding: utf-8 -*-

"""
This is document with steps for Training app
"""

from __future__ import unicode_literals
from time import sleep
from settings import base as settings
from selenium.webdriver.remote import webdriver


def before_all(context):
    context.browser = webdriver.WebDriver(
        settings.WEBDRIVER_URL,
        desired_capabilities=settings.DESIRED_CAPABILITIES
    )


def before_scenario(context, scenario):
    context.current_user = ''  # Place to hold current user login
    # Place to hold all users info:
    context.scenario_users = {
        'first_user': {
            'login': '',
            'password': '',
            'log_time': '',
        },
        'last_user': {
            'login': '',
            'password': '',
            'log_time': '',
        },
        'all_users': {
        },
    }


def after_step(context, step):
    sleep(0)  # Use this to slow down your steps


def after_all(context):
    context.browser.quit()

