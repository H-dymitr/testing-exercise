import requests
from behave import given, when, then

@given('the API endpoint is "{endpoint}"')
def step_given_api_endpoint(context, endpoint):
    context.endpoint = endpoint

@when('I create a user with name "{name}" and job "{job}"')
def step_create_user(context, name, job):
    payload = {
        "name": name,
        "job": job
    }
    context.response = requests.post(context.endpoint, json=payload)

@when('I get the user details')
def step_get_user_details(context):
    context.response = requests.get(context.endpoint)

@when('I register a user with email "{email}" and password "{password}"')
def step_register_user(context, email, password):
    payload = {
        "email": email,
        "password": password
    }
    context.response = requests.post(context.endpoint, json=payload)

@when('I login a user with email "{email}" and password "{password}"')
def step_login_user(context, email, password):
    payload = {
        "email": email,
        "password": password
    }
    context.response = requests.post(context.endpoint, json=payload)

@then('the status code should be {status_code:d}')
def step_check_status_code(context, status_code):
    assert context.response.status_code == status_code

@then('the response should contain the user id and createdAt')
def step_check_user_created_response(context):
    json_data = context.response.json()
    assert "id" in json_data
    assert "createdAt" in json_data

@then('the response should contain the user data')
def step_check_user_data_response(context):
    json_data = context.response.json()
    assert "data" in json_data

@then('the response should contain the user id and token')
def step_check_registration_response(context):
    json_data = context.response.json()
    assert "id" in json_data
    assert "token" in json_data

@then('the response should contain the token')
def step_check_login_response(context):
    json_data = context.response.json()
    assert "token" in json_data
