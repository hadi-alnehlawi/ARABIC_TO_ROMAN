from app import arabic_to_roman


class TestFailure:
    def test_str_input(self):
        assert arabic_to_roman("abcde") == "Not A Valid Arabic Integer"

    def test_input_0(self):
        assert arabic_to_roman("0") == "The Number Must Be Between 1 && 3999"

    def test_input_4000(self):
        assert arabic_to_roman("4000") == "The Number Must Be Between 1 && 3999"
