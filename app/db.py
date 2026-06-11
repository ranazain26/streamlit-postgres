import os
from sqlalchemy import create_engine
import pandas as pd

def get_engine():
    db_user = os.getenv("DB_USER", "app_user")
    db_password = os.getenv("DB_PASSWORD", "app_password")
    db_host = os.getenv("DB_HOST", "localhost") 
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "student_opportunities_db")
    
    conn_str = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    return create_engine(conn_str)

def run_query(query):
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql(query, conn)