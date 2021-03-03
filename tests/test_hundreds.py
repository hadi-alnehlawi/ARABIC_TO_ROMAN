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

    def test_774(self):
        assert arabic_to_roman(774) == "DCCLXXIV"

    def test_623(self):
        assert arabic_to_roman(623) == "DCXXIII"

    def test_264(self):
        assert arabic_to_roman(264) == "CCLXIV"

    def test_442(self):
        assert arabic_to_roman(442) == "CDXLII"

    def test_676(self):
        assert arabic_to_roman(676) == "DCLXXVI"

    def test_415(self):
        assert arabic_to_roman(415) == "CDXV"

    def test_215(self):
        assert arabic_to_roman(415) == "CCXV"
