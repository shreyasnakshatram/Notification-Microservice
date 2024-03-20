from peewee import PostgresqlDatabase
from configs.env import *
import logging
from contextvars import ContextVar

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
logger = logging.getLogger("peewee")

db = PostgresqlDatabase(
    DATABASE_NAME,
    autorollback=True,
    user = DATABASE_USER,
    password = DATABASE_PASSWORD
)