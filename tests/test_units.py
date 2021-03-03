from app import arabic_to_roman


class TestUnits:
    def test_1(self):
        assert arabic_to_roman(1) == "I"

    def test_2(self):
        assert arabic_to_roman(2) == "II"

    def test_3(self):
        assert arabic_to_roman(3) == "III"

    def test_4(self):
        assert arabic_to_roman(4) == "IV"

    def test_5(self):
        assert arabic_to_roman(5) == "V"

    def test_6(self):
        assert arabic_to_roman(6) == "VI"

    def test_7(self):
        assert arabic_to_roman(7) == "VII"

    def test_8(self):
        assert arabic_to_roman(8) == "VIII"

    def test_9(self):
        assert arabic_to_roman(9) == "IX"
