"""MODELS - PERSON ADDRESS
The address of a person is part of the Person model
"""
from typing import Optional

# # Package # #
from .common import BaseModel
from .fields import AddressFields

from .department import Department
from .province import Province
from .district import District

__all__ = ("Address", )


class Address(BaseModel):
    """The address information of a person"""
    department: Optional[Department]
    province: Optional[Province]
    distritct: Optional[District]
    street: str = AddressFields.street
