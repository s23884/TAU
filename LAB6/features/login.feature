Feature: Login on Social Media Platforms

  Scenario: Facebook Login
    Given I am on the Facebook login page
    When I enter valid credentials
    Then I should be logged in successfully on Facebook

  Scenario: Instagram Login
    Given I am on the Instagram login page
    When I enter valid credentials
    Then I should be logged in successfully on Instagram
