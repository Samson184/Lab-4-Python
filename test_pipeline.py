import string
import unittest

from analytics import count_words_in_file


def read_words(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().split()


class TestPipeline(unittest.TestCase):
    def test_input_file_not_empty(self):
        self.assertTrue(len(read_words("TF1_1.txt")) > 0)

    def test_output_has_no_punctuation(self):
        with open("TF1_2.txt", encoding="utf-8") as f:
            text = f.read()
        found = [ch for ch in text if ch in string.punctuation]
        self.assertEqual(found, [], f"Знайдено розділові знаки: {found}")

    def test_one_word_per_line(self):
        with open("TF1_2.txt", encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                self.assertEqual(len(line.split()), 1, f"Рядок {n}: не одне слово")

    def test_no_empty_lines(self):
        self.assertEqual(count_words_in_file("TF1_2.txt")["empty_lines"], 0)

    def test_word_count_matches_input(self):
        raw = read_words("TF1_1.txt")
        clean = [w.strip(string.punctuation) for w in raw]
        clean = [w for w in clean if w]
        self.assertEqual(count_words_in_file("TF1_2.txt")["words"], len(clean))


if __name__ == "__main__":
    unittest.main()