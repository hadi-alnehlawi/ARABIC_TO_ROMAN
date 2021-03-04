from app import arabic_to_roman


class TestFailure:
    def test_str_input_1(self):
        assert arabic_to_roman("abcde") == "Not A Valid Arabic Integer"
    
    def test_str_input_2(self):
        assert arabic_to_roman("133bc") == "Not A Valid Arabic Integer"

    def test_str_input_3(self):
        assert arabic_to_roman("de88") == "Not A Valid Arabic Integer"

    def test_str_input_4(self):
        assert arabic_to_roman("a88fe") == "Not A Valid Arabic Integer"

    def test_input_0(self):
        assert arabic_to_roman("0") == "The Number Must Be Between 1 && 3999"

    def test_input_4000(self):
        assert arabic_to_roman("4000") == "The Number Must Be Between 1 && 3999"

    def test_input_minus_1(self):
        assert arabic_to_roman("-1") == "The Number Must Be Between 1 && 3999"
