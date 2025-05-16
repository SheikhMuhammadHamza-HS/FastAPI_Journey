from fastapi.testclient import TestClient
from hello import addition

def test_addition():
    # print(f"The sum of {a} and {b} is: {res}")
    assert 0  == addition(0, 0)
    assert -6  == addition(-1, -5)
    assert 8  == addition(4, 4)
    assert 4  == addition(2, 2)