class true_false:
    def __init__(self, prompt, response, answer):
        self.prompt = prompt
        self.response = response
        self.answer = answer

    def true_false_answers(self, answer):
        return self == answer


class multiple_choice:
    def __init__(self, prompt, questions, answers):
        self.prompt = prompt
        self.questions = questions
        self.answers = answers

    def multiple_choice_answers(self, answers):
        return self == answers


class numerical:
    def __init__(self, prompt, num, answer):
        self.prompt = prompt
        self.num = num
        self.answer = answer

    def num_answer(self, answer):
        return self == answer


class fill_blank:
    def __init__(self, prompt, word, answer):
        self.prompt = prompt
        self.word = word
        self.answer = answer

    def fill_blank_answer(self, answer):
        return self == answer

