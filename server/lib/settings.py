#!/usr/bin/env python3
import os
from pydantic import BaseModel, ValidationError, validator


class Settings(BaseModel):
    egoDbHost: str
    egoDbUser: str
    egoDbPassword: str
    egoDbDatabase: str

    @validator("*", each_item=True)
    def emptyString(cls, elem):
        if isinstance(elem, str):
            if not elem or elem.isspace():
                raise ValueError("Variable is empty")
        return elem


settings = Settings(
    egoDbHost=os.getenv("EGORDB_DB_HOST"),
    egoDbDatabase=os.getenv("EGORDB_DB_DATABASE"),
    egoDbUser=os.getenv("EGORDB_DB_USER"),
    egoDbPassword=os.getenv("EGORDB_DB_PASSWORD"),
)
