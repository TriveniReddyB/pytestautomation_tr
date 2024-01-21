import pytest
import json
import os
from datetime import date, timedelta
from datetime import datetime
import requests

d = date.today()
dt = datetime.now()


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


def get_AllUsers_reqres():
    response = requests.get(
        fetch_data["APIURL"] + fetch_data["get_users"],
        headers=fetch_data["req_hearders"],
    )
    # verify status code
    assert response.status_code == 200
    req_response = response.json()

    print("Elapse time:", response.elapsed)

    # <pretty response JSON format>
    # response is in the form of object. before call keys in json format, parse response object.
    res_jsondata = json.dumps(req_response, indent=4)
    jsondata = json.loads(res_jsondata)
    usersDict = {}
    usersList = []
    for data in jsondata["data"]:
        if "Lindsay" in data["first_name"]:
            assert "Lindsay" == data["first_name"]
            assert "Lindsay" == data["first_name"]
            assert "Lindsay" == "triveni_failtest"
        usersList.append(data["first_name"])
    return usersList, usersDict


@pytest.fixture(scope="module")
def fixture_tests():
    print(f"Start execute Patterns for pre-processing test executions..!!{dt}")
    yield
    print(f"End execute Pattern for post-processing test results..!!{dt}")


@pytest.mark.Regression
@pytest.mark.Smoke
def test_EN001_search():
    print("this is test_EN001_search")
    mylist, mydict = get_AllUsers_reqres()
    print("result is:", mylist, mydict)


@pytest.mark.Regression
@pytest.mark.Smoke
def test_EN002_keywordsearch():
    print("this is test_EN002_keywordsearch")


@pytest.mark.Regression
def test_EN003_savedsearch():
    print("this is test_EN003_savedsearch")


@pytest.mark.Regression
@pytest.mark.Smoke
def test_EN004_refinesearch():
    print("this is test_EN004_refinesearch")


# @pytest.mark.Regression
@pytest.mark.skip("Skipping test as it is depends on workflow tests")
def test_EN005_wfsearch():
    print("this is test_EN005_wfsearch")


@pytest.mark.Regression
@pytest.mark.Smoke
def test_EN006_multisearch():
    print("this is test_EN006_multisearch")


@pytest.mark.Regression
def test_EN007_filtersearch():
    print("this is test_EN007_filtersearch")


@pytest.mark.Regression
def test_EN008_entitytype_search():
    print("this is test_EN008_entitytype_search")


@pytest.mark.Regression
@pytest.mark.Smoke
def test_EN009_search():
    print("this is test_EN009_search")
    list1 = [0, 1, 4, 3, 7, 8, 9, 10, 8, 3, 1, 2, 0, 4]
    for i in list1:
        print(i)


@pytest.mark.Regression
@pytest.mark.Smoke
def test_EN010_search():
    print("this is test_EN010_search")


@pytest.mark.Regression
@pytest.mark.Smoke
def test_EN011_search():
    print("this is test_EN011_search:")
    formatDate = dt.strftime("%d/%m/%y_%H:%M:%S")
    if d.month == 12:
        print("this month have 31 days...", date.today().month)
    else:
        print("this month have 30 days", formatDate)
