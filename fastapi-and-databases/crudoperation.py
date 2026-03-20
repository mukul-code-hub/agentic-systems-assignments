from db import engine
from tables import student
from sqlalchemy import insert, update, delete

def insert_student(input_name:str , input_age:int , input_city: str):
    with engine.connect() as conn:
        query = insert(student).values(name = input_name, age = input_age, city = input_city)
        conn.execute(query)
        conn.commit()

def update_student(input_name :str, input_city : str):
    with engine.connect() as conn:
        query = update(student).where(student.c.name == input_name).values(city = input_city)
        conn.execute(query)
        conn.commit()

def delete_student(input_age : int):
    with engine.connect() as conn:
        query = delete(student).where(student.c.age <= input_age)
        conn.execute(query)
        conn.commit()
