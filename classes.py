class true_false:
    def __init__(self, prompt, response):
        self.prompt = prompt
        self.response = response


class multiple_choice:
    def __init__(self, prompt, qone, qtwo, qthree, qfour, qfive):
        self.prompt = prompt


class numerical:
    def __init__(self, prompt, num):
        self.prompt = prompt
        self.num = num

    def num_answer(self, num):
        return


class fill_blank:
    def __init__(self, prompt, word):
        self.prompt = prompt
        self.word = word
