from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from bug_tracker.settings import Settings

##TODO: criar uma variavel de ambiente no .env e um arquivo de settings.
engine = create_engine(Settings().DATABASE_URL) 


def get_session():
    with Session(engine) as session:
        yield session