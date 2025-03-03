import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from typing import AsyncGenerator

load_dotenv()

class Database:
    def __init__(self):
        self.engine = create_async_engine(url=os.getenv('DATABASE_URL'), echo=False)
        self.session = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )


db = Database()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with db.session() as session:
        yield session