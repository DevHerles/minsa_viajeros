"""MODELS - PERSON - READ
Person Read model. Inherits from PersonCreate and adds the person_id field, which is the _id field on Mongo documents
"""

# # Native # #
from datetime import date, datetime
from typing import Optional, List
from people_api.models.alarm_signal_update import AlarmSignal

# # Installed # #
import pydantic
from dateutil.relativedelta import relativedelta

# # Package # #
from .person_create import ContactCreate
from .person_update import ContactUpdate
from .fields import ContactFields
from .person_address import Address
from .person_comorbidity import Comorbidity
from .person_symptoms import Symptoms
from .person_eess import Eess

__all__ = ("ContactRead", "ContactsRead")


class ContactRead(ContactUpdate):
    """Body of Person GET and POST responses"""
    contact_id: Optional[str] = ContactFields.person_id
    parent_contact_id: Optional[str] = ContactFields.person_id
    doc_type: Optional[str] = ContactFields.doc_type
    doc_number: Optional[str] = ContactFields.doc_number
    name: Optional[str] = ContactFields.name
    first_name: Optional[str] = ContactFields.first_name
    last_name: Optional[str] = ContactFields.last_name
    birth: Optional[date] = ContactFields.birth
    start_date: Optional[date] = ContactFields.start_date
    alternative_cellphone_number: Optional[
        str] = ContactFields.alternative_cellphone_number
    cellphone_number: Optional[str] = ContactFields.cellphone_number
    address: Optional[Address]
    comorbidity: Optional[Comorbidity]
    symptoms: Optional[List[Symptoms]]
    # eess: Optional[Eess]
    # alarm_signal: Optional[AlarmSignal]

    @pydantic.root_validator(pre=True)
    def _set_contact_id(cls, data):
        """Swap the field _id to person_id (this could be done with field alias, by setting the field as "_id"
        and the alias as "contact_id", but can be quite confusing)"""
        document_id = data.get("_id")
        if document_id:
            data["contact_id"] = document_id
        return data

    @pydantic.root_validator()
    def _set_age(cls, data):
        """Calculate the current age of the person from the date of birth, if any"""
        birth = data.get("birth")
        if birth:
            today = datetime.now().date()
            data["age"] = relativedelta(today, birth).years
        return data

    class Config(ContactCreate.Config):
        extra = pydantic.Extra.ignore  # if a read document has extra fields, ignore them


ContactsRead = List[ContactRead]
