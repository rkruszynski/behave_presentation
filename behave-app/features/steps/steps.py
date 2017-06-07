# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Steps for Training app
"""

from page_objects import page_objects_dict, find_element
from behave import given, when, then
from time import strftime
from settings import base as settings


@when('I click "{xpath_name}" element')
def step_impl(context, xpath_name):
    find_element(context, xpath_name).click()


@when('I type "{text}" in "{element}" element')
def step_impl(context, text, element):
    find_element(context, element).send_keys(text)


@given('I open main page')
def step_impl(context):
    context.browser.get(settings.PAGE_URLS['mainPage'])


@when('I open add new user page')
def step_impl(context):
    find_element(context, 'new_user').click()


@then('I can see "{text}" in "{element}" element')
def step_impl(context, text, element):
    text_on_element = find_element(context, element).text.strip()
    message = 'Your element has "{}" instead of "{}"'.format(text_on_element, text)
    assert text_on_element == text, message


@when('I create user with "{username}" username and "{password}" password')
def step_impl(context, username, password):
    context.execute_steps(
        """
        When I click "new_user" element
        When I type "{login}" in "new_user_username" element
        When I type "{password}" in "new_user_password" element
        When I click "new_user_submit" element
        """.format(login=username, password=password)
    )


@when('I create {usertype} user with "{username}" username and "{password}" password')
def step_impl(context, usertype, username, password):
    context.execute_steps(
        """
        When I click "new_user" element
        """
    )
    if usertype == "admin":
        find_element(context, 'new_user_is_admin').click()

    context.execute_steps(
        """
        When I type "{login}" in "new_user_username" element
        When I type "{password}" in "new_user_password" element
        When I click "new_user_submit" element
        """.format(login=username, password=password)
    )


@given('I log in as "{login}" user with "{password}" password')
def step_impl(context, login, password):
    context.execute_steps(
        """
    When I type "{login}" in "login_username_field" element
    When I type "{password}" in "login_password_field" element
    When I click "login_button" element
        """.format(login=login, password=password)
    )

    hello_message = "Hello {user}".format(user=login)
    context.execute_steps(
        """
        Then I can see "{message}" in "logged_user" element
        """.format(message=hello_message)
    )
    context.current_user = login  # save login to context

    now = strftime("%H:%M")

    if context.scenario_users['first_user']['login'] == '':  # JUST FIRST USER
        context.scenario_users['first_user']['login'] = login
        context.scenario_users['first_user']['password'] = password
        context.scenario_users['first_user']['log_time'] = now
    else:
        context.scenario_users['last_user']['login'] = login  # JUST LAST USER
        context.scenario_users['last_user']['password'] = password
        context.scenario_users['last_user']['log_time'] = now

    context.scenario_users['all_users'][str(login)] = {}  # ALL USERS
    context.scenario_users['all_users'][str(login)]['login'] = login
    context.scenario_users['all_users'][str(login)]['password'] = password
    context.scenario_users['all_users'][str(login)]['log_time'] = now


@then('I check log data for all users')
def step_impl(context):
    find_element(context, 'logs').click()
    # I don't check if admin has correct login time. But I forgot why ;)
    # You can easily remove list comprehension and below iterate through all keys
    users = [x for x in context.scenario_users['all_users'].keys() if x != 'admin']
    for user in users:
        find_element(context, 'search_box').send_keys(user)
        find_element(context, 'search_button').click()
        page_logged_time = str(find_element(context, 'last_log_time').text)
        context_logged_time = context.scenario_users['all_users'][user]['log_time']
        message = 'User: "{}" In context: "{}" and on page: "{}"'.format(user, context_logged_time, page_logged_time)
        assert context_logged_time in page_logged_time, message
