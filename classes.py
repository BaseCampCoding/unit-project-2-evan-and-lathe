class true_false:
    def __init__(self, prompt, response, answer):
        self.prompt = prompt
        self.response = response


class multiple_choice:
    def __init__(self, prompt, qone, qtwo, qthree, qfour, qfive):
        self.prompt = prompt


class numerical:
    def __init__(self, prompt, num, answr):
        self.prompt = prompt
        self.num = num

    def num_answer(self, num, answr):
        return num == answr


class fill_blank:
    def __init__(self, prompt, word, answr):
        self.prompt = prompt
        self.word = word

