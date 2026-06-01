import os
from psycopg import connect

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    conn = connect(DATABASE_URL, autocommit=True)
else:
    conn = None  # Fallback to mock or in-memory
