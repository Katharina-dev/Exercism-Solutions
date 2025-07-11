class Allergies:

    allergy = {0:'eggs', 1:'peanuts', 2:'shellfish', 3:'strawberries',
           4:'tomatoes', 5:'chocolate', 6:'pollen', 7:'cats'}

    def __init__(self, score):
        self.score = f'{score:b}'[-1:-9:-1]
        self._lst = [Allergies.allergy[i] for i in range(len(self.score)) if self.score[i] == '1']

    def allergic_to(self, item):
        return item in self._lst

    @property
    def lst(self):
        return self._lst
