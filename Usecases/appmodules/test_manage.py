import pytest
import json
import os
import requests
from datetime import date, timedelta
from datetime import datetime

absolute_path = os.path.dirname(__file__)
inputfile = "appdata.json"
# testinput = os.path.join(absolute_path, inputfile)
testinput = absolute_path + "\\..\\..\\" + inputfile
try:
    with open(testinput, "r") as getinput:
        urldata = getinput.read()
        fetch_data = json.loads(urldata)
except FileNotFoundError:
    print("File error occurred.")
except Exception as e:
    print("this is runtime exception", e)


def get_SingleUserNotFound():
    response = requests.get(
        fetch_data["APIURL"] + fetch_data["single_user_notfound"],
        headers=fetch_data["req_hearders"],
    )
    req_response = response.json()
    # print("req_response", req_response)
    # verify status code
    assert response.status_code == 404
    assert len(req_response) == 0


@pytest.mark.Regression
@pytest.mark.Smoke
def test_EM100_txt_attribute():
    print("this is test_EM100_txt_attribute")


@pytest.mark.Smoke
def test_EM101_txtarea_attribute():
    print("this is test_EM101_txtarea_attribute")
    for x in range(9):
        print(f"Range of val:'{x}'")


@pytest.mark.Regression
@pytest.mark.Smoke
@pytest.mark.workflow
def test_EM102_richttext_attribute():
    print("this is test_EM102_richttext_attribute")
    for ele in [10, 20, 300]:
        print(ele)
    print("Get element", ele)


@pytest.mark.skip("Skipping test as LOV attribute has open issue")
@pytest.mark.Smoke
def test_EM103_lov_attribute():
    print("this is test_EM103_lov_attribute")


@pytest.mark.Regression
@pytest.mark.Smoke
def test_EM104_lov_colle_attribute():
    print("this is test_EM104_lov_colle_attribute")
    for z in range(1, 20, 5):
        print(f"Increment range of values:'{z}'")
