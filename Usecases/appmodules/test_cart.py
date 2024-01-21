import pytest


@pytest.mark.Regression
@pytest.mark.Smoke
def test_CART200():
    print("this is test_CART200")


@pytest.mark.Regression
def test_test_CART201():
    print("this is test_test_CART201")


@pytest.mark.Regression
@pytest.mark.Sanity
def test_CART202():
    print("this is test_CART202")
