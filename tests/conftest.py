import pytest
from stuff.accum import Accumulator

@pytest.fixture
def accum(scope="function"):
    yield Accumulator()
    print("cleanup step")

# @pytest.fixture(scope="function") #the browser will open and close in each test
# def driver():
#     driver = webdriver