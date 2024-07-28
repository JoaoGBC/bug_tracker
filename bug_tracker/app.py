from fastapi import FastAPI
from pydantic import BaseModel
from bug_tracker.routes.aplication_adm_users import aplication_adm_users
from bug_tracker.settings import Settings

app = FastAPI()




app.include_router(aplication_adm_users.router)

