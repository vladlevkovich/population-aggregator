import asyncio
import httpx
import pandas as pd
from io import StringIO
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db_connect import db
from app.db.models import CountryPopulation

URL = 'https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_(United_Nations)&oldid=1215058959'

async def fetch_data_population(url):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            df = pd.read_html(StringIO(response.text), header=0)[0]
            df = df[['Location', 'UN Statistical Subregion[1]', 'Population (1 July 2023)']].rename(
                columns={'Location': 'Location', 'UN Statistical Subregion[1]': 'Region', 'Population (1 July 2023)': 'Population'}
            )
            df = df.dropna(subset=['Population', 'Region'])
            df['Population'] = df['Population'].astype(str).str.replace(',', '').str.extract('(\d+)')[0].astype(int)    # конвертуємо в число
            return df.to_dict(orient='records')
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
        return []
    except httpx.RequestError as e:
        print(f"Request error occurred: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

async def save_data_population_to_db(db: AsyncSession):
    try:
        data = await fetch_data_population(URL)
        for entry in data:
            country = CountryPopulation(
                country=entry['Location'],
                region=entry['Region'],
                population=entry['Population']
            )
            db.add(country)
            await db.commit()
        return {'message': 'Saved'}
    except ValueError as e:
        print(f"Value error: {e}")
        return {'message': f"Error: {e}"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'message': f"Error: {e}"}


async def main():
    async with db.session() as session:
        res = await save_data_population_to_db(session)
        return res

if __name__ == '__main__':
    asyncio.run(main())
