Feature: Create users

  Scenario: 3: Create admin user and log in
    Given I open main page
    When I type "admin" in "login_username_field" element
    When I type "test1234" in "login_password_field" element
    When I click "login_button" element
    Then I can see "Hello admin" in "logged_user" element
    When I create admin user with "Adminuser" username and "test1234" password
    When I click "logged_user" element
    When I click "logout_button" element
    When I type "Adminuser" in "login_username_field" element
    When I type "test1234" in "login_password_field" element
    When I click "login_button" element
    Then I can see "Hello Adminuser" in "logged_user" element
    When I click "logged_user" element
    When I click "logout_button" element
