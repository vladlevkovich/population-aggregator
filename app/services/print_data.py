from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db_connect import db
from sqlalchemy import text
import asyncio


async def get_population(db: AsyncSession):
    try:
        query = text("""
            SELECT region,
               SUM(population) AS total_population,
               MAX(country) FILTER (WHERE population = (SELECT MAX(population) FROM population p2 WHERE p2.region = p1.region)) AS largest_country,
               MAX(population) FILTER (WHERE population = (SELECT MAX(population) FROM population p2 WHERE p2.region = p1.region)) AS largest_population,
               MAX(country) FILTER (WHERE population = (SELECT MIN(population) FROM population p2 WHERE p2.region = p1.region)) AS smallest_country,
               MIN(population) FILTER (WHERE population = (SELECT MIN(population) FROM population p2 WHERE p2.region = p1.region)) AS smallest_population
            FROM population p1
            GROUP BY region
            ORDER BY total_population DESC;
        """)
        result = await db.execute(query)
        rows = result.fetchall()

        data = [dict(row._mapping) for row in rows]
        return data
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

async def main():
    async with db.session() as session:
        data = await get_population(session)
        for entry in data:
            print(f"{entry['region']}\n{entry['total_population']}\n"
                  f"{entry['largest_country']}\n{entry['largest_population']}\n"
                  f"{entry['smallest_country']}\n{entry['smallest_population']}\n")

if __name__ == '__main__':
    asyncio.run(main())

