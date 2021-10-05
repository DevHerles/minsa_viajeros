"""MODELS - PERSON - CREATE
Person Create model. Inherits from PersonUpdate, but all the required fields must be re-defined
"""
from typing import Optional, List

# # Package # #
from .person_update import ContactUpdate
from .person_address import Address
from .fields import ContactFields, ComorbidityFields, AddressFields

__all__ = ("ContactCreate", )


class ContactCreate(ContactUpdate):
    """Body of Person POST requests"""
    name: str = ContactFields.name
    first_name: str = ContactFields.first_name
    last_name: Optional[str] = ContactFields.last_name
    alternative_cellphone_number: str = ContactFields.alternative_cellphone_number
    doc_type: str = ContactFields.doc_type
    doc_number: str = ContactFields.doc_number
    # Birth remains Optional, so is not required to re-declare
