from app import arabic_to_roman


class TestThousands:
    def test_1000(self):
        assert arabic_to_roman(1000) == "M"

    def test_2000(self):
        assert arabic_to_roman(2000) == "MM"

    def test_3000(self):
        assert arabic_to_roman(3000) == "MMM"

    def test_2034(self):
        assert arabic_to_roman(2034) == "MMXXXIV"

    def test_3461(self):
        assert arabic_to_roman(3461) == "MMMCDLXI"

    def test_1853(self):
        assert arabic_to_roman(1853) == "MDCCCLIII"

    def test_3825(self):
        assert arabic_to_roman(3825) == "MMMDCCCXXV"

    def test_3302(self):
        assert arabic_to_roman(3302) == "MMMCCCII"

    def test_1539(self):
        assert arabic_to_roman(1539) == "MDXXXIX"

    def test_2405(self):
        assert arabic_to_roman(2405) == "MMCDV"

    def test_1871(self):
        assert arabic_to_roman(1871) == "MDCCCLXXI"

    def test_3933(self):
        assert arabic_to_roman(3933) == "MMMCMXXXIII"

    def test_2265(self):
        assert arabic_to_roman(2265) == "MMCCLXV"

    def test_3026(self):
        assert arabic_to_roman(3026) == "MMMXXVI"

    def test_1999(self):
        assert arabic_to_roman(1999) == "MCMXCIX"

    def test_1492(self):
        assert arabic_to_roman(1492) == "MCDXCII"

    def test_1550(self):
        assert arabic_to_roman(1550) == "MDL"
