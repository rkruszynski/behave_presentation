Feature: Create users

  Scenario: 1: Create two users and check if they can log in
    Given I open main page
    When I type "admin" in "login_username_field" element
    When I type "test1234" in "login_password_field" element
    When I click "login_button" element
    Then I can see "Hello admin" in "logged_user" element
    When I click "new_user" element
    When I type "newuser" in "new_user_username" element
    When I type "test1234" in "new_user_password" element
    When I click "new_user_submit" element
    When I click "logged_user" element
    When I click "logout_button" element
    When I type "newuser" in "login_username_field" element
    When I type "test1234" in "login_password_field" element
    When I click "login_button" element
    Then I can see "Hello newuser" in "logged_user" element
    When I click "logged_user" element
    When I click "logout_button" element
    When I type "admin" in "login_username_field" element
    When I type "test1234" in "login_password_field" element
    When I click "login_button" element
    Then I can see "Hello admin" in "logged_user" element
    When I click "new_user" element
    When I type "newuser2" in "new_user_username" element
    When I type "test1234" in "new_user_password" element
    When I click "new_user_submit" element
    When I click "logged_user" element
    When I click "logout_button" element
    When I type "newuser2" in "login_username_field" element
    When I type "test1234" in "login_password_field" element
    When I click "login_button" element
    Then I can see "Hello newuser2" in "logged_user" element

