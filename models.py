################################################
# This file is used to define the models for the application. Do not alter this file.
################################################
from pydantic import BaseModel
from typing import Optional


# new task model
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


# read task model
class TaskRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
