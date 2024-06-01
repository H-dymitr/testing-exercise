Feature: Get user details
  Scenario: Successfully get a user details
    Given the API endpoint is "https://reqres.in/api/users/1"
    When I get the user details
    Then the status code should be 200
    And the response should contain the user data