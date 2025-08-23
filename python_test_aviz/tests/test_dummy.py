import pytest

@pytest.mark.dummy
class TestDummy:
    def test_dummy(self):
        assert True

    @pytest.mark.dummy
    def test_true(self):
        assert True


@pytest.mark.dummy
def test_true():
    assert True
