Feature: User login
  Scenario: Successfully login a user
    Given the API endpoint is "https://reqres.in/api/login"
    When I login a user with email "eve.holt@reqres.in" and password "cityslicka"
    Then the status code should be 200
    And the response should contain the token