from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import QueuePool
import os
from dotenv import load_dotenv
import pyodbc
import urllib.parse

load_dotenv()

# Azure SQL Database connection string format:
# mssql+aioodbc://username:password@server.database.windows.net/database?driver=ODBC+Driver+18+for+SQL+Server
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine with proper Azure SQL configuration
engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # Set to False in production
    pool_size=5,  # Adjust based on your needs
    max_overflow=10,
    pool_timeout=30,
    pool_pre_ping=True,  # Enable connection health checks
    pool_recycle=1800,  # Recycle connections after 30 minutes
    fast_executemany=True,  # Optimize bulk operations
    connect_args={
        "timeout": 30,
        "connection_timeout": 30,
        "retry_with_dsn_on_error": True,
    }
)

# Create async session factory
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

# Create declarative base
Base = declarative_base()

# Dependency to get DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

# Initialize database
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Health check function
async def check_db_connection():
    try:
        async with AsyncSessionLocal() as session:
            await session.execute("SELECT 1")
            return True
    except Exception as e:
        print(f"Database connection error: {e}")
        return False 