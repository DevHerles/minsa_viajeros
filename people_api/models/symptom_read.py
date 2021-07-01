"""MODELS - PERSON - READ
Person Read model. Inherits from PersonCreate and adds the person_id field, which is the _id field on Mongo documents
"""

# # Native # #
from datetime import datetime
from typing import Optional, List

# # Installed # #
import pydantic
from dateutil.relativedelta import relativedelta

# # Package # #
from .symptom_create import SymptomCreate
from .fields import SymptomFields

__all__ = ("SymptomRead", "SymptomsRead")


class SymptomRead(SymptomCreate):
    """Body of Symptom GET and POST responses"""
    person_id: str = SymptomFields.person_id
    symptom_id: str = SymptomFields.symptom_id
    q1: str = SymptomFields.q1
    q2: str = SymptomFields.q2
    q3: str = SymptomFields.q3
    q4: str = SymptomFields.q4
    q5: str = SymptomFields.q5
    q6: str = SymptomFields.q6
    q7: str = SymptomFields.q7
    q8: str = SymptomFields.q8
    q9: str = SymptomFields.q9
    q10: str = SymptomFields.q10
    latitude: Optional[str] = SymptomFields.latitude
    longitude: Optional[str] = SymptomFields.longitude

    @pydantic.root_validator(pre=True)
    def _set_symptom_id(cls, data):
        """Swap the field _id to symptom_id (this could be done with field alias, by setting the field as "_id"
        and the alias as "symptom_id", but can be quite confusing)"""
        document_id = data.get("_id")
        if document_id:
            data["symptom_id"] = document_id
        return data

    class Config(SymptomCreate.Config):
        extra = pydantic.Extra.ignore  # if a read document has extra fields, ignore them


SymptomsRead = List[SymptomRead]
