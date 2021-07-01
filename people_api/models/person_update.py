"""MODELS - PERSON - UPDATE
Person Update model. All attributes are set as Optional, as we use the PATCH method for update
(in which only the attributes to change are sent on request body)
"""

# # Native # #
from datetime import date
from typing import Optional, List
from contextlib import suppress

# # Package # #
from .common import BaseModel
from .fields import PersonFields, AddressFields, ComorbidityFields
from .person_address import Address
from .person_comorbidity import Comorbidity
from .person_symptoms import Symptoms

__all__ = ("PersonUpdate", )


class PersonUpdate(BaseModel):
    """Body of Person PATCH requests"""
    name: Optional[str] = PersonFields.name
    birth: Optional[date] = PersonFields.birth
    doc_number: Optional[str] = PersonFields.doc_number
    doc_type: Optional[str] = PersonFields.doc_type
    first_name: Optional[str] = PersonFields.first_name
    last_name: Optional[str] = PersonFields.last_name
    person_id: Optional[str] = PersonFields.person_id
    phone_number: Optional[str] = PersonFields.phone_number
    street: str = AddressFields.street
    city: str = AddressFields.city
    state: str = AddressFields.state
    zip_code: str = AddressFields.zip_code
    q1: str = ComorbidityFields.q1
    q2: str = ComorbidityFields.q2
    q3: str = ComorbidityFields.q3
    q4: str = ComorbidityFields.q4
    q5: str = ComorbidityFields.q5
    q6: str = ComorbidityFields.q6
    q7: str = ComorbidityFields.q7
    q8: str = ComorbidityFields.q8
    q9: str = ComorbidityFields.q9
    q10: str = ComorbidityFields.q10
    q11: str = ComorbidityFields.q11
    q12: str = ComorbidityFields.q12
    q13: str = ComorbidityFields.q13
    q14: str = ComorbidityFields.q14
    q15: str = ComorbidityFields.q15
    q16: str = ComorbidityFields.q16

    def dict(self, **kwargs):
        # The "birth" field must be converted to string (isoformat) when exporting to dict (for Mongo)
        # TODO Better way to do this? (automatic conversion can be done with Config.json_encoders, but not available for dict
        d = super().dict(**kwargs)
        with suppress(KeyError):
            d["birth"] = d.pop("birth").isoformat()
        return d
