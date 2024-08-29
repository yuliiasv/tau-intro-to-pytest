import pytest
from stuff.accum import Accumulator

@pytest.fixture
def accum(scope="function"):
    yield Accumulator()
    print("cleanup step")