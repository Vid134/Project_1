import json
import os

def get_test_data(testcase_name):
    file_path = os.path.join("testdata", "login_data.json")

    with open(file_path) as file:
        data = json.load(file)

    return data[testcase_name]

