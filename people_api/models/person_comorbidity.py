"""MODELS - PERSON COMORBIDITY
The comorbidity of a person is part of the Person model
"""

# # Native # #
from datetime import date
from typing import Optional
from contextlib import suppress

# # Package # #
from .common import BaseModel
from .fields import ComorbidityFields

__all__ = ("Comorbidity", )


class Comorbidity(BaseModel):
    """The comorbidity information of a person"""
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
    created: Optional[date] = ComorbidityFields.created
    updated: Optional[date] = ComorbidityFields.updated

    def dict(self, **kwargs):
        # The "birth" field must be converted to string (isoformat) when exporting to dict (for Mongo)
        # TODO Better way to do this? (automatic conversion can be done with Config.json_encoders, but not available for dict
        d = super().dict(**kwargs)
        with suppress(KeyError):
            d["created"] = d.pop("created").isoformat()
            d["updated"] = d.pop("updated").isoformat()
        return d
