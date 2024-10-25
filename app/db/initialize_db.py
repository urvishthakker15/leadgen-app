import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from models import Base  # Import your models from the file where Lead is defined

load_dotenv()

# Get the synchronous DATABASE_URL from the environment variable
SYNC_DATABASE_URL = os.getenv("SYNC_DATABASE_URL")

# Create a synchronous engine using the SYNC_DATABASE_URL
engine = create_engine(SYNC_DATABASE_URL, echo=True)

# Create the tables in the database
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")
