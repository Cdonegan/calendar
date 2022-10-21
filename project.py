class Project:

    def __init__(self, description=None, time_to_complete=None, target_finish_date=None, task=None, dependency=None, date_range=None):
        # declare variables in here
        self.description = description
        self.time_to_complete = time_to_complete
        self.target_finish_date = target_finish_date
        self.dependency = dependency
        self.task = task
        self.date_range = date_range

    def create_project(self):
        self.description = "connor is the best"
        self.time_to_complete = 10
        self.target_finish_date = "march/5/2023"
        self.dependency = "{'1': 15, '2':3}"
        self.task = "{'1': 1, '2':7}"
        self.date_range = "6/7/2022 - 7/7/2022"

    def user_input_of_project(self):
        """take some user input about the project
        """


