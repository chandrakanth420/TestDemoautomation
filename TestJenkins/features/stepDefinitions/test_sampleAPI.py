import logging
import os
from os.path import dirname

import requests
import json
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from utilities.global_variables import GlobalVariables

logging.basicConfig(level=logging.INFO)

GlobalVariables.project_path = dirname(dirname(__file__))
GlobalVariables.feature_file_path = os.path.join(GlobalVariables.project_path, "user_creation.feature")


class TestingError(RuntimeError):
    pass


class Test:
    URL = " "
    payload = """{
        'name' : 'anti',
        'job' : 'programmer'
        'last_name' : 'sam'
    }"""
    get_response = " "
    post_response = " "


@scenario(GlobalVariables.feature_file_path, 'Creating an User using a Sample API')
def test_creating_an_user_using_a_sample_api():
    """Creating an User using a Sample API."""


@given('URI for sample API')
def uri_for_sample_api():
    """URI for sample API."""
    Test.URL = 'https://reqres.in/api/users'
    logging.info("URI for API is %s : ", Test.URL)


@when('I perform POST and GET Requests')
def i_perform_post_and_get_requests():
    """I perform POST and GET Requests."""
    Test.post_response = requests.post(Test.URL, data=Test.payload)
    post_json_responce = Test.post_response.json()
    logging.info("JSON Responce for POST request is %s :", post_json_responce)
    o_id = post_json_responce.get("id")
    logging.info("OID is %s : ", o_id)
    Test.get_response = requests.get(Test.URL + o_id)
    get_json_responce = Test.get_response.json()
    logging.info("JSON Responce for GET request is %s :" + json.dumps(get_json_responce, indent=4))


@then('i should see the Responce Code and Responce JSON')
def i_should_see_the_responce_code_and_responce_json():
    """i should see the Responce Code and Responce JSON."""
    logging.info("Response code for POST Request %s : ", Test.post_response)
    logging.info("Response code for GET Request with OID is %s : ", Test.get_response)
