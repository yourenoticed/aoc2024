class TaskBase():
    def __init__(self, input_file: str) -> None:
        self.input = self.parse_input(input_file)

    def parse_input(self, input_file: str) -> list[str]:
        with open(input_file, "r") as file:
            return file.read().split("\n")

    def task_1(self):
        pass

    def task_2(self):
        pass
