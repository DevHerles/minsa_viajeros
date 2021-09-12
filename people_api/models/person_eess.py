"""MODELS - PERSON SYMPTOMS
The symptoms of a person is part of the Person model
"""

# # Native # #
from datetime import date
from typing import Optional
from contextlib import suppress

# # Package # #
from .common import BaseModel
from .fields import EessFields

__all__ = ("Eess", )


class Eess(BaseModel):
    """The EESS information of a person"""
    code: str = EessFields.code
    name: str = EessFields.name
