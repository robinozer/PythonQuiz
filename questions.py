class Option():
    def __init__(self, id, name):   # constructor function using self
        self.id = id  # variable using self.
        self.name = name  # variable using self.


class Question():
    def __init__(self, question, options):   # constructor function using self
        self.question = question  # variable using self.
        self.options = options


questions_list = [
    Question("hej", [Option(1, "röd"), Option(2, "blå")]),
    Question("test", [Option(1, "röd"), Option(2, "blå")])]
