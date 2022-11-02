"""CP1404/CP5632 Practical - Programming Language"""


class ProgrammingLanguage:
    def __init__(self, name=, typing, reflection, year):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"