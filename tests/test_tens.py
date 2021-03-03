from app import arabic_to_roman


class TestTens:
    def test_10(self):
        assert arabic_to_roman(10) == "X"

    def test_20(self):
        assert arabic_to_roman(20) == "XX"

    def test_30(self):
        assert arabic_to_roman(30) == "XXX"

    def test_40(self):
        assert arabic_to_roman(40) == "XL"

    def test_50(self):
        assert arabic_to_roman(50) == "L"

    def test_60(self):
        assert arabic_to_roman(60) == "LX"

    def test_70(self):
        assert arabic_to_roman(70) == "LXX"

    def test_80(self):
        assert arabic_to_roman(80) == "LXXX"

    def test_90(self):
        assert arabic_to_roman(90) == "XC"

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
