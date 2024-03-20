from database.db_session import db_state_default, db
from fastapi import Depends
import time

async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()

def get_db():
    try:
        db.connect(reuse_if_open=True)
        yield db
    finally:
        if not db.is_closed():
            db.close()