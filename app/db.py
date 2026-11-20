import json
from contextlib import contextmanager
import psycopg
from psycopg.rows import dict_row
from app.config import settings


@contextmanager
def get_db_connection():
    url = settings.DATABASE_URL
    if not url:
        raise ValueError("DATABASE_URL is not set in the environment variables.")
    with psycopg.connect(url, row_factory=dict_row) as conn:
        yield conn


def audit(conn, actor, tenant, action, details):
    conn.execute(
        "INSERT INTO audit_events (actor, tenant_id, action, detail) VALUES (%s, %s, %s, %s)",
        (actor, tenant, action, json.dumps(details)),
    )
