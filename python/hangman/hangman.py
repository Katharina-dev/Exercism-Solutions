# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'
class Hangman:
    def __init__(self, word):
        self.word = word
        self.mask = list('_' * len(self.word))
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")
        guess = False
        for i in range(len(self.word)):
            if self.word[i] == char and self.mask[i] != char:
                self.mask[i] = char
                guess = True
        self.remaining_guesses = self.remaining_guesses if guess else self.remaining_guesses-1
        
        
    def get_masked_word(self):
        return ''.join(self.mask)
    def get_status(self):
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        elif '_' not in self.mask:
            self.status = STATUS_WIN
        return self.status
