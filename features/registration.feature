Feature: Register a user
  Scenario: Successfully register a user
    Given the API endpoint is "https://reqres.in/api/register"
    When I register a user with email "eve.holt@reqres.in" and password "pistol"
    Then the status code should be 200
    And the response should contain the user id and token
