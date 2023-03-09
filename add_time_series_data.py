from database.time_series import Data,Session
import random

def add_data(id, date_time, value):
    session = Session()
    row = Data(id=id, date_time=date_time, value=value)
    session.add(row)
    session.close()
    session.commit()

for i in range(100):
    print(random.random())
