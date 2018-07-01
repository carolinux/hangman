import unittest


class Hangman(object):

    INITIAL_TRIES = 9

    def __init__(self, word):
        self._word = word
        self.tries = self.INITIAL_TRIES
        self._is_win = True
        self._shown_text = ['_'] * len(self._word)


    @property
    def shown_text(self):
        return ' '.join(self._shown_text)

    @property
    def is_win(self):
        return self._is_win

    def guess_word(self, word):
        if self.tries > 0 and self._word == word:
            self._is_win = True
        self.tries-=1

    def guess_letter(self, char):
        # here we don't check if the player has already checked the character before
        if self.tries > 0 and char in self._word:
            for i, c in enumerate(self._word):
                if char == c:
                    self._shown_text[i] = char

        self.tries-=1

    def is_over(self):
        return self.is_win or self.tries > 0


class TestHangman(unittest.TestCase):

    def test_wrong_letter_guess(self):
        game = Hangman('bottle')
        game.guess_letter('a')
        self.assertEquals(game.shown_text, '_ _ _ _ _ _')
        self.assertEquals(game.tries, 8)

    def test_correct_letter_guess(self):
        game = Hangman('bottle')
        game.guess_letter('t')
        self.assertEquals(game.shown_text, '_ _ t t _ _')
        self.assertEquals(game.tries, 8)

    def test_correct_word_guess(self):
        game = Hangman('bottle')
        game.guess_letter('t')
        game.guess_word('bottle')
        self.assertEquals(game.is_win, True)
        self.assertEquals(game.tries, 7)
        self.assertTrue(game.is_win)
        self.assertTrue(game.is_over)




