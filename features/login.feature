Feature: Login functionality

  Scenario: Login with valid credentials
    Given I am on the login page
    When I login with valid username and password
    Then I should be redirected to the trips page