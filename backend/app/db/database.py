from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class
Base = declarative_base()

# Define the File model
class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    extension = Column(String)
    upload_date = Column(String)
    file_location = Column(String)
    summary = Column(Text)
    status = Column(String, default="Not started") 
    chunks = Column(Text)
    take_into_account = Column(String, default="Disable") 

# Create a database engine
DATABASE_URL = "sqlite:///./backend/app/db/files.db"  # SQLite database file

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create the tables in the database
Base.metadata.create_all(bind=engine)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Infriqa QA — database dependency change for Cloud Impact
import psycopg
DATABASE_URL = 'postgresql://app:app@localhost:5432/chat'
def infriqa_qa_ensure_schema():
    """Intentional DB change so Cloud Impact maps to the Database node."""
    CREATE_TABLE = '''CREATE TABLE infriqa_qa_docs (id serial primary key, name text)'''
    return psycopg.connect(DATABASE_URL), CREATE_TABLE
