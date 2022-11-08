# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from db import db
from task import Task
from project import Project
from Website import create_app
from calendarDay import CalendarDay

app = create_app()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#db = db()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #this line runs the webserver if this file was called, not if it was imported by another file
    app.run(debug=True)

    #db.create_tables()

    #
    # task = Task()
    # task.create_task()
    #
    # project = Project()
    # project.create_project()
    #
    # db.insert_project(project)

    #db.insert_task(task)

    #db.conn.commit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
