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
    q1: bool = ComorbidityFields.q1
    q2: bool = ComorbidityFields.q2
    q3: bool = ComorbidityFields.q3
    q4: bool = ComorbidityFields.q4
    q5: bool = ComorbidityFields.q5
    q6: bool = ComorbidityFields.q6
    q7: bool = ComorbidityFields.q7
    q8: bool = ComorbidityFields.q8
    q9: bool = ComorbidityFields.q9
    q10: bool = ComorbidityFields.q10
    q11: bool = ComorbidityFields.q11
    q12: bool = ComorbidityFields.q12
    q13: bool = ComorbidityFields.q13
    q14: bool = ComorbidityFields.q14
    q15: bool = ComorbidityFields.q15
    q16: bool = ComorbidityFields.q16
