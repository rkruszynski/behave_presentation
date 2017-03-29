# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import parse
from behave import given, when, then, use_step_matcher, register_type
from page_objects import page_objects_dict
from time import sleep

"""
Parsed steps for Training app
"""

use_step_matcher("cfparse")


@parse.with_pattern(r"\sadmin")
def parse_admin(text):
    """Getting element from gherkin function call
    example: ' admin' will trigger this parser
    param text: string - like example
    return: string "admin"
    """
    return "admin"


@parse.with_pattern(r'\s"\w*"\slocation')
def parse_location(text):
    """Getting element from gherkin function call
    example: ' "Poznan" location' will trigger this parser
    param text: string - like example
    return: string with location name
    """
    return text.split('"')[1]


@parse.with_pattern(r'\swith\sphone\snumber\s"\d+"')
def parse_phone_number(text):
    """Getting element from gherkin function call
    example: ' with phone number "123456"' will trigger this parser
    param text: string - like example
    return: string with just number
    """
    return text.split('"')[1]


register_type(
    admin=parse_admin,
    location=parse_location,
    phone_number=parse_phone_number,
)


@when('I create new{admin:admin?} user with "{login}" login "{password}" password{phone_number:phone_number?}{location:location?}')
def step_impl(context, admin, login, password, phone_number, location):
    """
    Usage: When I create create new user with "ABCD" login "test1234" password with phone number "123456"

    :param str login: new user login
    :param str password: new user password
    :param str " admin" set user as admin
    :param int phone_number: telefone number (up to 9 digits)
    """
    new_user_xpath = page_objects_dict['new_user']
    context.browser.find_element_by_xpath(new_user_xpath).click()
    new_user_login_xpath = page_objects_dict['new_user_username']
    context.browser.find_element_by_xpath(new_user_login_xpath).send_keys(login)
    new_user_password_xpath = page_objects_dict['new_user_password']
    context.browser.find_element_by_xpath(new_user_password_xpath).send_keys(password)

    if admin:
        is_admin_xpath = page_objects_dict['new_user_is_admin']
        context.browser.find_element_by_xpath(is_admin_xpath).click()
    if location:
        is_location_xpath = page_objects_dict['new_user_location']
        context.browser.find_element_by_xpath(is_location_xpath).send_keys(location)
    if phone_number:
        phone_number_xpath = page_objects_dict['phone_number']
        context.browser.find_element_by_xpath(phone_number_xpath).clear()
        context.browser.find_element_by_xpath(phone_number_xpath).send_keys(phone_number)

    submit_button = page_objects_dict['new_user_submit']
    context.browser.find_element_by_xpath(submit_button).click()
