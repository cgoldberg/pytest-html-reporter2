import pytest


@pytest.fixture()
def setup():
    yield


def test_pass(setup):
    assert True


def test_fail(setup):
    assert False
