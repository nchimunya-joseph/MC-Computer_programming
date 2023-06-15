import unittest
import hangman

class HangmanGameTests(unittest.TestCase):
    def start_game(self):
        hangman()

    def test_start_game(self):
        self.start_game()
        self.assertTrue(hangman.word in hangman.word_list)
        self.assertTrue(hangman.guessed_letters, [])
        self.assertEqual(hangman.attempts, 6)

    def test_guess_letter_correct(self):
        self.start_game()
        self.word = "apple"
        result = self.guess_letter("a")
        self.assertEqual(result, "a____")

if __name__ == "__main__":
    unittest.main()