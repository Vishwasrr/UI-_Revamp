import pytest

scenarios = [(1, 2, 3), (4, 5, 6), (7, 8, 15)]


# alternately we can have, ex: logins: [('abc@gmail.com', 'pass1'), ('xyz@gmail.com', 'pass2')...]
# @pytest.mark.parametrize("username, password", logins)

@pytest.mark.parametrize("a, b, c", scenarios)
def test_add(a, b, c):
    assert a + b == c
