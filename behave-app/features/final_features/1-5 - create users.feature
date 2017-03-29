Feature: Create users

  Scenario: 2: Create two users and check if they can log in
    Given I open main page
    When I type "admin" in "login_username_field" element
    When I type "test1234" in "login_password_field" element
    When I click "login_button" element
    Then I can see "Hello admin" in "logged_user" element
    When I create new admin user with "nowy_administrator2" login "test1234" password "poznan" location
    When I click "logged_user" element
    When I click "logout_button" element
    When I type "Adminuser" in "login_username_field" element
    When I type "test1234" in "login_password_field" element
    When I click "login_button" element
    Then I can see "Hello Adminuser" in "logged_user" element
    When I click "logged_user" element
    When I click "logout_button" element
