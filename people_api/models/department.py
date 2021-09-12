"""MODELS - PERSON SYMPTOMS
The symptoms of a person is part of the Person model
"""

# # Native # #
from datetime import date
from typing import Optional
from contextlib import suppress

# # Package # #
from .common import BaseModel
from .fields import DepartmentFields

__all__ = ("Department", )


class Department(BaseModel):
    """The Department information of a person"""
    code: str = DepartmentFields.code
    name: str = DepartmentFields.name
