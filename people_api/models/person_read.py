"""MODELS - PERSON - READ
Person Read model. Inherits from PersonCreate and adds the person_id field, which is the _id field on Mongo documents
"""

# # Native # #
from datetime import date, datetime
from typing import Optional, List

# # Installed # #
import pydantic
from dateutil.relativedelta import relativedelta

# # Package # #
from .person_create import PersonCreate
from .person_update import PersonUpdate
from .fields import PersonFields
from .person_address import Address
from .person_comorbidity import Comorbidity
from .person_symptoms import Symptoms
from .person_eess import Eess

__all__ = ("PersonRead", "PeopleRead")


class PersonRead(PersonUpdate):
    """Body of Person GET and POST responses"""
    contact_id: Optional[str] = PersonFields.person_id
    parent_contact_id: Optional[str] = PersonFields.person_id
    doc_type: Optional[str] = PersonFields.doc_type
    doc_number: Optional[str] = PersonFields.doc_number
    name: Optional[str] = PersonFields.name
    first_name: Optional[str] = PersonFields.first_name
    last_name: Optional[str] = PersonFields.last_name
    birth: Optional[date] = PersonFields.birth
    phone_number: Optional[str] = PersonFields.phone_number
    cellphone_number: Optional[str] = PersonFields.cellphone_number
    address: Optional[Address]
    comorbidity: Optional[Comorbidity]
    symptoms: Optional[List[Symptoms]]
    eess: Optional[Eess]

    @pydantic.root_validator(pre=True)
    def _set_person_id(cls, data):
        """Swap the field _id to person_id (this could be done with field alias, by setting the field as "_id"
        and the alias as "person_id", but can be quite confusing)"""
        document_id = data.get("_id")
        if document_id:
            data["person_id"] = document_id
        return data

    @pydantic.root_validator()
    def _set_age(cls, data):
        """Calculate the current age of the person from the date of birth, if any"""
        birth = data.get("birth")
        if birth:
            today = datetime.now().date()
            data["age"] = relativedelta(today, birth).years
        return data

    class Config(PersonCreate.Config):
        extra = pydantic.Extra.ignore  # if a read document has extra fields, ignore them


PeopleRead = List[PersonRead]
