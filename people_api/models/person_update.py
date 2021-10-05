"""MODELS - PERSON - UPDATE
Person Update model. All attributes are set as Optional, as we use the PATCH method for update
(in which only the attributes to change are sent on request body)
"""

# # Native # #
from datetime import date
from typing import Optional, List
from contextlib import suppress

from people_api.models.alarm_signal_update import AlarmSignal

# # Package # #
from .common import BaseModel
from .fields import ContactFields, AddressFields, ComorbidityFields, SymptomFields
from .person_address import Address
from .person_comorbidity import Comorbidity
from .person_symptoms import Symptoms
from .person_eess import Eess

__all__ = ("ContactUpdate", )


class ContactUpdate(BaseModel):
    """Body of Person PATCH requests"""
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

    def dict(self, **kwargs):
        # The "birth" field must be converted to string (isoformat) when exporting to dict (for Mongo)
        # TODO Better way to do this? (automatic conversion can be done with Config.json_encoders, but not available for dict
        d = super().dict(**kwargs)
        with suppress(KeyError):
            d["birth"] = d.pop("birth").isoformat()
            d["start_date"] = d.pop("start_date").isoformat()
        return d
