from db import engine
from sqlalchemy import Table, MetaData , Column , Integer , String, CheckConstraint

metadata = MetaData()

student = Table("student",
                metadata,
                Column("id", Integer, primary_key = True),
                Column("name", String(50), nullable = False),
                Column("age", String(50)),
                Column("city", String(50), nullable = True),
                CheckConstraint('age > 18')
                )

def create_all_table():
    metadata.create_all(engine)