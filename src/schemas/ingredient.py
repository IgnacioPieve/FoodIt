from pydantic import BaseModel


class IngredientAddUpdateSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class IngredientSchema(IngredientAddUpdateSchema):
    id: str
    class Config:
        orm_mode = True
