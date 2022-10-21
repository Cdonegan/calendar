from sqlalchemy import text

sql_text = text("CREATE TABLE task(id SERIAL PRIMARY KEY, description VARCHAR, time_to_complete FLOAT, "
                "target_finish_date VARCHAR, date_range VARCHAR);")
sql_text = text("CREATE TABLE project (id SERIAL PRIMARY KEY, description VARCHAR, time_to_complete FLOAT, dependency "
                "VARCHAR, task VARCHAR, date_range VARCHAR);")
sql_text = text("CREATE TABLE calendar_day (day DATE PRIMARY KEY, description VARCHAR, project VARCHAR, task VARCHAR, "
                "dependencies VARCHAR );")
sql_text = text("CREATE TABLE dependency (id SERIAL PRIMARY KEY, description VARCHAR, project VARCHAR, task VARCHAR, "
                "time_period_affecting_work VARCHAR, date_range VARCHAR );")
