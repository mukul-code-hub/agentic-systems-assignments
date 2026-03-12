# Design a Pydantic model system with the following requirements:

# Address Model

# city → string (minimum length 3)
# pincode → string (must be exactly 6 digits)
# User Model

# user_id → integer
# name → string
# email → email string
# age → integer (must be ≥ 18)
# address → nested Address model
# is_premium → optional boolean (default = False)
# Assignment validation should be enabled

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Address(BaseModel):
    city:str = Field(..., min_length=3)
    pincode : str = Field(..., pattern=r"^\d[9]$")

class user(BaseModel):
    user_id : int
    name: str
    email: EmailStr
    age : int = Field(ge=18)
    address: Address
    is_premium: Optional[bool] = False

data = user[user_id=1, nam
