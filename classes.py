class true_false:
    def __init__(self, prompt, response, answer):
        self.prompt = prompt
        self.response = response
        self.answer = answer

class multiple_choice:
    def __init__(self, prompt, questions, answers):
        self.prompt = prompt
        self.questions = questions
        self.answers = answers


class numerical:
    def __init__(self, prompt, num, answer):
        self.prompt = prompt
        self.num = num

    def num_answer(self, answr):
        return self == answr


class fill_blank:
    def __init__(self, prompt, word, answer):
        self.prompt = prompt
        self.word = word
        self.answer = answer

    def fill_blank_answer(self,)


