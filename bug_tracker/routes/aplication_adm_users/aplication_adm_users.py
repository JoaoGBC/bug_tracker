from http import HTTPStatus
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from bug_tracker.database import get_session
from bug_tracker.models.user_adm_moodel import AplicationUserAdm
from bug_tracker.routes.aplication_adm_users.schemas import AplicationUserAdmSchema, PublicAplicationUserAdmSchema
from bug_tracker.settings import Settings


router = APIRouter(prefix="/adm-users", tags=['adm-users'])

T_Session = Annotated[Session, Depends(get_session)]

class Message(BaseModel):
    message: str


@router.post('/', response_model=Message)
def create_adm_user(user: AplicationUserAdmSchema, session: T_Session):
    
    ## verifica se o email existe no banco de dados, 
    # pra falhar a operação logo inicio
    # db_user = session.scalar(select(AplicationUserAdm).where(AplicationUserAdm.email == user.email))
    # if db_user:
    #     raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='Email already exists.')
    
    # db_user = AplicationUserAdm(**user.model_dump())
    # session.add(db_user)
    # session.commit()
    # session.refresh(db_user)
    return {'message' : Settings().DATABASE_URL}
    return db_user
    ...



