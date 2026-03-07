# Run pip3 install fastapi pydantic uvicorn
# Run the application uvicorn main:app --reload

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/search")
def search_for_name(name: str = Query(description="Please enter the name", default="Deepak"),
                                        age: int = Query(description="Please enter the age", default=30)):
    data = {"name": name, "age": age}
    return data

