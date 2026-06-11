from typing import List, Dict, Any
from .db import conn_cursor


def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS opportunities (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        company TEXT,
        value NUMERIC,
        status TEXT,
        deadline DATE,
        created_at TIMESTAMP DEFAULT now()
    );
    """
    with conn_cursor() as (conn, cur):
        cur.execute(sql)


def add_opportunity(data: Dict[str, Any]) -> int:
    sql = """
    INSERT INTO opportunities (title, company, value, status, deadline)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING id
    """
    with conn_cursor() as (conn, cur):
        cur.execute(sql, (data.get("title"), data.get("company"), data.get("value"), data.get("status"), data.get("deadline")))
        row = cur.fetchone()
        return row["id"]


def list_opportunities() -> List[Dict[str, Any]]:
    sql = "SELECT * FROM opportunities ORDER BY created_at DESC"
    with conn_cursor() as (conn, cur):
        cur.execute(sql)
        return cur.fetchall()


def get_opportunity(opportunity_id: int) -> Dict[str, Any]:
    sql = "SELECT * FROM opportunities WHERE id = %s"
    with conn_cursor() as (conn, cur):
        cur.execute(sql, (opportunity_id,))
        return cur.fetchone()


def update_opportunity(opportunity_id: int, data: Dict[str, Any]) -> None:
    sql = """
    UPDATE opportunities
    SET title = %s, company = %s, value = %s, status = %s, deadline = %s
    WHERE id = %s
    """
    with conn_cursor() as (conn, cur):
        cur.execute(sql, (data.get("title"), data.get("company"), data.get("value"), data.get("status"), data.get("deadline"), opportunity_id))


def delete_opportunity(opportunity_id: int) -> None:
    sql = "DELETE FROM opportunities WHERE id = %s"
    with conn_cursor() as (conn, cur):
        cur.execute(sql, (opportunity_id,))
