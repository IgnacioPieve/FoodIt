from fastapi import APIRouter, Depends

from dependencies import auth
from schemas.ingredient import IngredientAddUpdateSchema, IngredientSchema
from models.ingredient import Ingredient

router = APIRouter(prefix="/ingredient", tags=["Ingredient"])


@router.get("", status_code=200, response_model=list[IngredientSchema], include_in_schema=False)
@router.get("/", status_code=200, response_model=list[IngredientSchema], summary="Get ingredients")
async def get_ingredients(authentication=Depends(auth.authenticate)):
    """
    Get user ingredients
    """
    user, _ = authentication
    return user.ingredients


@router.post("", status_code=200, response_model=IngredientSchema, include_in_schema=False)
@router.post("/", status_code=200, response_model=IngredientSchema, summary="Add ingredient")
async def add_ingredient(
        ingredient: IngredientAddUpdateSchema,
        authentication=Depends(auth.authenticate)
):
    """
    Add ingredient
    """
    user, db = authentication
    ingredient = Ingredient(**ingredient.dict(), user=user)
    db.add(ingredient)
    db.commit()
    return ingredient

