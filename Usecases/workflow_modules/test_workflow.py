import pytest


@pytest.mark.Regression
@pytest.mark.Sanity
@pytest.mark.Smoke
def test_WF_600():
    print("this is test_WF_600")


@pytest.mark.Regression
def test_WF_601():
    print("this is test_WF_601")


@pytest.mark.Regression
@pytest.mark.Sanity
@pytest.mark.Search
def test_WF_602():
    print("this is test_WF_601")


@pytest.mark.Regression
@pytest.mark.Smoke
def test_WF_603():
    print("this is test_WF_601")
    # returns all items to result variable except the items on intersection
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    xresult = x.symmetric_difference(y)
    yresult = y.symmetric_difference(x)
    print("Set x & y symmetric_difference in x is:", xresult)
    print("Set x & y symmetric_difference in y is:", yresult)
    assert xresult == yresult
