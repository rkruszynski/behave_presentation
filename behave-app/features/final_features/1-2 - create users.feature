Feature: Create users

  Scenario Outline: 2: Create two users and check if they can log in
    Given I open main page
    When I type "admin" in "login_username_field" element
    When I type "test1234" in "login_password_field" element
    When I click "login_button" element
    Then I can see "Hello admin" in "logged_user" element
    When I create user with "<Login>" username and "<Password>" password
    When I click "logged_user" element
    When I click "logout_button" element
    When I type "<Login>" in "login_username_field" element
    When I type "<Password>" in "login_password_field" element
    When I click "login_button" element
    Then I can see "Hello <Login>" in "logged_user" element
    When I click "logged_user" element
    When I click "logout_button" element

  Examples: Users
    | Login | Password |
    | newuser1 | test1234 |
    | newuser2 | test1234 |