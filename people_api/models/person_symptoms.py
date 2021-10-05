"""MODELS - PERSON SYMPTOMS
The symptoms of a person is part of the Person model
"""

# # Native # #
from datetime import date, datetime
from typing import Optional
from contextlib import suppress

import pydantic

from people_api.models.alarm_signal_update import AlarmSignal

# # Package # #
from .common import BaseModel
from .fields import SymptomFields

__all__ = ("Symptoms", )


class Symptoms(BaseModel):
    """The symptoms information of a person"""
    q1: bool = SymptomFields.q1
    q2: bool = SymptomFields.q2
    q3: bool = SymptomFields.q3
    q4: bool = SymptomFields.q4
    q5: bool = SymptomFields.q5
    q6: bool = SymptomFields.q6
    q7: bool = SymptomFields.q7
    q8: bool = SymptomFields.q8
    q9: bool = SymptomFields.q9
    q10: Optional[str] = SymptomFields.q10
    is_suspicious: bool = SymptomFields.is_suspicious
    created: Optional[date] = SymptomFields.created_at
    updated: Optional[date] = SymptomFields.updated_at
    alarm_signal: Optional[AlarmSignal]
    latitude: Optional[str] = SymptomFields.latitude
    longitude: Optional[str] = SymptomFields.longitude

    @pydantic.root_validator()
    def _set_age(cls, data):
        """Calculate the current age of the person from the date of birth, if any"""
        today = datetime.now().date()
        data["created"] = today
        data["updated"] = today
        return data

    def dict(self, **kwargs):
        # The "birth" field must be converted to string (isoformat) when exporting to dict (for Mongo)
        # TODO Better way to do this? (automatic conversion can be done with Config.json_encoders, but not available for dict
        d = super().dict(**kwargs)
        with suppress(KeyError):
            d["created"] = d.pop("created").isoformat()
            d["updated"] = d["created"]
        return d
