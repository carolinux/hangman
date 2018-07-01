import unittests















class TestHangman(unittest.TestCase):

    def test_wrong_letter_guess(self):
        game = HangMan('bottle')
        game.guess_letter('a')
        self.assertEquals(game.shown_text, '_ _ _ _ _ _')
        self.assertEquals(game.tries, 8)

    def test_correct_letter_guess(self):
        game = HangMan('bottle')
        game.guess_letter('t')
        self.assertEquals(game.shown_text, '_ _ t t _ _')
        self.assertEquals(game.tries, 8)

    def test_correct_word_guess(self):
        game = HangMan('bottle')
        game.guess_letter('t')
        game.guess_word('bottle')
        self.assertEquals(game.is_win, True)
        self.assertEquals(game.tries, 7)


