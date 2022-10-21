


class Task:

    def __init__(self, description = None, time_to_complete = None, target_finish_date = None):
        #declare variables in here
        self.description = description
        self.time_to_complete = time_to_complete
        self.target_finish_date = target_finish_date

    def create_task(self):

        '''     self.description = input("enter the description?")
        self.time_to_complete = input("how many hours to complete?")
        self.target_finish_date =input("What is the target finish date?")'''

        self.description = "connor is the best"
        self.time_to_complete = 10
        self.target_finish_date = "march/5/2023"
