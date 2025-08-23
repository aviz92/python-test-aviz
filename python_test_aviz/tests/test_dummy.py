import pytest


@pytest.mark.dummy
class TestDummy:
    def test_dummy(self) -> None:
        assert True

    @pytest.mark.dummy
    def test_true(self) -> None:
        assert True


@pytest.mark.dummy
def test_true() -> None:
    assert True
