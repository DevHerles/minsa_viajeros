"""MODELS - SYMPTOM - CREATE
Symptom Create model. Inherits from SymptomUpdate, but all the required fields must be re-defined
"""
from typing import Optional, List

# # Package # #
from .symptom_update import SymptomUpdate
from .fields import SymptomFields

__all__ = ("SymptomCreate", )


class SymptomCreate(SymptomUpdate):
    """Body of Symptom POST requests"""
    person_id: str = SymptomFields.person_id
    latitude: str = SymptomFields.latitude
    longitude: str = SymptomFields.longitude
    # Birth remains Optional, so is not required to re-declare
