# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
Parsed steps for Training app
"""

import parse
from behave import given, when, then, use_step_matcher, register_type
from page_objects import page_objects_dict, find_element
from time import sleep

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
    find_element(context, 'new_user').click()
    find_element(context, 'new_user_username').send_keys(login)
    find_element(context, 'new_user_password').send_keys(password)

    if admin:
        find_element(context, 'new_user_is_admin').click()
    if location:
        find_element(context, 'new_user_location').send_keys(location)
    if phone_number:
        phone_number = find_element(context, 'phone_number')
        phone_number.clear()
        phone_number.send_keys(phone_number)

    find_element(context, 'new_user_submit').click()
