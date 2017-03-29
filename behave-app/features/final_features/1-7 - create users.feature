Feature: Create users

  Scenario: 2: Create two users and check if they can log in
    Given I open main page
    Given I log in as "admin" user with "test1234" password
    When I create new admin user with "new_admin1" login "test1234" password
    When I click "logged_user" element
    When I click "logout_button" element
    Given I log in as "new_admin1" user with "test1234" password
    When I click "logged_user" element
    When I click "logout_button" element
   Given I log in as "admin" user with "test1234" password
    When I create new admin user with "new_admin2" login "test1234" password "poznan" location
    When I click "logged_user" element
    When I click "logout_button" element
    Given I log in as "new_admin2" user with "test1234" password
    Then I check log data for all users