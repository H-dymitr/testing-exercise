Feature: Create a user
  Scenario: Successfully create a user
    Given the API endpoint is "https://reqres.in/api/users"
    When I create a user with name "John" and job "Developer"
    Then the status code should be 201
    And the response should contain the user id and createdAt