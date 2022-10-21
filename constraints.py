class Constraints:

    def __init__(self, description=None, time_to_complete=None, impact_time=None, tasks=None, dependencies=None, date_range=None, project=None):
        # declare variables in here
        self.tasks = tasks
        self.description = description
        self.time_to_complete = time_to_complete
        self.impact_time = impact_time
        self.dependencies = dependencies
        self.date_range = date_range
        self.project = project

