# Pydantic for Data Validation - Subjective
from pydantic import BaseModel, Field, EmailStr

class UserRegister(BaseModel):
    username: str = Field(min_length=5, description="Username minimum lenght is 5")
    email: EmailStr =Field(description="Enter the valid email address")
    age: int = Field(ge = 18)

#Validate incoming data
user_info = {"username":"Samuel", "email":"abc@gmail.com", "age":19 }

try:
    user_object =  UserRegister(**user_info)
    print(user_object)
except ValueError as e:
    print( "The error is : " + str(e))


    