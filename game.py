from player import Player
player = Player()
class Game:
    def __init__(self):
        self.flags = {}
        self.variables = {}

    def dialogue(self, speaker, lines):
        if isinstance(lines, str):
            lines = [lines]
        print(f"{speaker}:")
        for line in lines:
            print(f"    {line}")
        input("    Press Enter to continue...")

    def input_dialogue(self, line, choices):
        if isinstance(choices, str):
            choices = [choices]

        for i, value in enumerate(choices):
            print(f"    {i+1}: {value}")

        while True:
            try:
                num = int(input(f"    {line}: "))
                if 1 <= num <= len(choices):
                    return str(num)
                else:
                    print("    Please enter a valid choice.")
                    pass
            except ValueError:
                print("    Please enter a valid number.")