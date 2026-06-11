from app.db import get_engine
from sqlalchemy import text

def execute_write(query, params=None):
    engine = get_engine()
    with engine.begin() as conn:
        conn.execute(text(query), params or {})

def delete_opportunity_by_id(op_id):
    query = "DELETE FROM opportunities WHERE opportunity_id = :id"
    execute_write(query, {"id": op_id})
