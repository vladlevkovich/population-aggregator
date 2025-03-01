from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.print_data import get_population
from app.services.get_data import save_data_population_to_db
from app.db.db_connect import get_db

router = APIRouter()

@router.get('/population')
async def get_all_population(db: AsyncSession = Depends(get_db)):
    try:
        res = await get_population(db)
        return {'data': res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@router.post('/parse-population')
async def parse_population(db: AsyncSession = Depends(get_db)):
    try:
        return await save_data_population_to_db(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
