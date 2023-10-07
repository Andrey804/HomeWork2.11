from datetime import date
from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    firstname: str = Field(max_length=30)
    lastname: str = Field(max_length=30)
    phone_number: str = Field(max_length=20)
    email: EmailStr
    born_date: date


class ContactUpdate(ContactModel):
    firstname: str = Field(max_length=30)
    lastname: str = Field(max_length=30)
    phone_number: str = Field(max_length=20)
    email: EmailStr
    born_date: date


class ContactResponse(ContactModel):
    id: int
    firstname: str = Field(max_length=30)
    lastname: str = Field(max_length=30)
    phone_number: str = Field(max_length=20)
    email: EmailStr
    born_date: date

    class Config:
        from_attributes = True  # UserWarning: Valid config keys have changed in V2: 'orm_mode' has been renamed to 'from_attributes'