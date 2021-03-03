from app import arabic_to_roman


class TestHundreds:
    def test_100(self):
        assert arabic_to_roman(100) == "C"

    def test_200(self):
        assert arabic_to_roman(200) == "CC"

    def test_300(self):
        assert arabic_to_roman(300) == "CCC"

    def test_400(self):
        assert arabic_to_roman(400) == "CD"

    def test_500(self):
        assert arabic_to_roman(500) == "D"

    def test_600(self):
        assert arabic_to_roman(600) == "DC"

    def test_700(self):
        assert arabic_to_roman(700) == "DCC"

    def test_800(self):
        assert arabic_to_roman(800) == "DCCC"

    def test_900(self):
        assert arabic_to_roman(900) == "CM"

    def test_301(self):
        assert arabic_to_roman(301) == "CCCI"
