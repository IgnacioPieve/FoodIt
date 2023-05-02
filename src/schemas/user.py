from pydantic import BaseModel, EmailStr


class UserUpdateSchema(BaseModel):
    fullname: str | None

    class Config:
        orm_mode = True


class UserSchema(UserUpdateSchema):
    id: str
    email: EmailStr

    class Config:
        orm_mode = True
