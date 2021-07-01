"""MODELS - PERSON - CREATE
Person Create model. Inherits from PersonUpdate, but all the required fields must be re-defined
"""
from typing import Optional, List

# # Package # #
from .person_update import PersonUpdate
from .person_address import Address
from .fields import PersonFields, ComorbidityFields, AddressFields

__all__ = ("PersonCreate", )


class PersonCreate(PersonUpdate):
    """Body of Person POST requests"""
    name: str = PersonFields.name
    first_name: str = PersonFields.first_name
    last_name: str = PersonFields.last_name
    phone_number: str = PersonFields.phone_number
    doc_type: str = PersonFields.doc_type
    doc_number: str = PersonFields.doc_number
    # Birth remains Optional, so is not required to re-declare
