import psycopg2
import psycopg2.extras
import csv
from task import Task
from project import Project
from constraints import Constraints
from calendarDay import CalendarDay
from sqlalchemy import create_engine
from sqlalchemy import text

db_string = "postgresql://postgres:everyone@localhost:5432/calendar"

# Windows work
db_name = 'calendar'
db_user = 'postgres'
db_password = 'everyone'
db_host = 'localhost'
db_port = '5432'


class db:
    '''

    '''

    def __init__(self):
        self.totals = {}

        # self.conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host)
        # self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        print(f'crating table TRANX')
        self.conn = create_engine(db_string)

        # self.cur.execute("CREATE TABLE TRANX (id SERIAL PRIMARY KEY, name VARCHAR, total FLOAT, date DATE, type VARCHAR, inputfiletype VARCHAR);")

        # response = cur.fetchall()
        # self.conn.commit()

    def create_tables(self):
        try:
            sql_text = text(
                "CREATE TABLE dependency (id SERIAL PRIMARY KEY, description VARCHAR, project VARCHAR, task VARCHAR, "
                "time_period_affecting_work VARCHAR, date_range VARCHAR );")
            try:
                with self.conn.connect() as conn:
                    conn.execute(sql_text)
            except Exception as e:
                print(f"{str(e)}")

        except Exception as e:
            print(f"connor {str(e)}")

    def insert_project(self, project: Project):
        try:
            sql_first = text('SELECT id FROM project order by id desc')
            with self.conn.connect() as conn:
                result = conn.execute(sql_first).fetchone()

            sql_text = text('INSERT INTO project (id, description, time_to_complete, dependency, task, date_range) '
                            'VALUES(:id, :description, :time_to_complete, :dependency, :task, :date_range);')
            params = {
                "id": result[0] + 1 if result is not None else 1,
                "description": project.description,
                "time_to_complete": project.time_to_complete,
                "dependency": project.dependency,
                "task": project.task,
                "date_range": project.date_range
            }

            with self.conn.connect() as conn:
                conn.execute(sql_text, params)

        except Exception as e:
            print(f"connor {str(e)}")

    def insert_task(self, task: Task):
        try:
            sql_first = text('SELECT id FROM task order by id desc')
            with self.conn.connect() as conn:
                result = conn.execute(sql_first).fetchone()

            sql_text = text('INSERT INTO task (id,target_finish_date, time_to_complete, description) VALUES(:id, '
                            ':target_finish_date, :time_to_complete, :description);')
            params = {
                "id": result[0] + 1 if result is not None else 1,
                "target_finish_date": task.target_finish_date,
                "description": task.description,
                "time_to_complete": task.time_to_complete
            }

            with self.conn.connect() as conn:
                conn.execute(sql_text, params)
                conn.session.commit()
        except Exception as e:
            print(f"connor {str(e)}")

    def insert_calendar_day(self, calendar_day: CalendarDay):
        try:
            sql_first = text('SELECT id FROM calendar_day order by id desc')
            with self.conn.connect() as conn:
                result = conn.execute(sql_first).fetchone()

            sql_text = text('INSERT INTO calendar_day (id, description, time_to_complete, dependency, task, date_range) '
                            'VALUES(:id, :description, :time_to_complete, :dependency, :task, :date_range);')
            params = {
                "id": result[0] + 1 if result is not None else 1,
                "description": calendar_day.description,
                "time_to_complete": calendar_day.time_to_complete,
                "dependency": calendar_day.dependency,
                "task": calendar_day.task,
                "date_range": calendar_day.date_range
            }

            with self.conn.connect() as conn:
                conn.execute(sql_text, params)

        except Exception as e:
            print(f"connor {str(e)}")

    def insert_constraint(self, constraints: Constraints):
        try:
            sql_first = text('SELECT id FROM dependency order by id desc')
            with self.conn.connect() as conn:
                result = conn.execute(sql_first).fetchone()

            sql_text = text('INSERT INTO dependency (id,description, project, task, time_period_affecting_work, date_range) VALUES(:id, '
                            ':description, :project, :task, :time_period_affecting_work, :date_range);')
            params = {
                "id": result[0] + 1 if result is not None else 1,
                "description": constraints.description,
                "time_to_complete": constraints.time_to_complete,
                "project": constraints.project,
                "task": constraints.tasks,
                "time_period_affecting_work": constraints.impact_time,
                "date_range": constraints.date_range
            }

            with self.conn.connect() as conn:
                conn.execute(sql_text, params)
                conn.session.commit()
        except Exception as e:
            print(f"connor {str(e)}")
        except:
            pass
