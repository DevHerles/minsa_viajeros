"""MODELS - PERSON SYMPTOMS
The symptoms of a person is part of the Person model
"""

# # Native # #
from datetime import date
from typing import Optional
from contextlib import suppress

# # Package # #
from .common import BaseModel
from .fields import SymptomsFields

__all__ = ("Symptoms", )


class Symptoms(BaseModel):
    """The symptoms information of a person"""
    q1: str = SymptomsFields.q1
    q2: str = SymptomsFields.q2
    q3: str = SymptomsFields.q3
    q4: str = SymptomsFields.q4
    q5: str = SymptomsFields.q5
    q6: str = SymptomsFields.q6
    q7: str = SymptomsFields.q7
    q8: str = SymptomsFields.q8
    q9: str = SymptomsFields.q9
    q10: str = SymptomsFields.q10
    created: Optional[date] = SymptomsFields.created
    updated: Optional[date] = SymptomsFields.updated

    def dict(self, **kwargs):
        # The "birth" field must be converted to string (isoformat) when exporting to dict (for Mongo)
        # TODO Better way to do this? (automatic conversion can be done with Config.json_encoders, but not available for dict
        d = super().dict(**kwargs)
        with suppress(KeyError):
            d["created"] = d.pop("created").isoformat()
            d["updated"] = d.pop("updated").isoformat()
        return d
