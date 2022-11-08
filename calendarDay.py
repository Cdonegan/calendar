class CalendarDay:

    def __init__(self, day=None, task=None, project=None, time_in_the_day=None, time_spent_working=None):
        self.day = day
        self.task = task
        self.project = project
        self.time_in_the_day = time_in_the_day
        self.time_spent_working = time_spent_working
        pass
        # declare anything on initilization of the object

    def print_contents(self):
        print("hello world")

    def add_values(self, a, b) -> int:
        return a + b