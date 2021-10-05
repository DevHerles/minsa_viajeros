from typing import Optional

from people_api.models.fields import AlarmSignalFields

from .common import BaseModel

class AlarmSignal(BaseModel):
  q1: bool = AlarmSignalFields.q1
  q2: bool = AlarmSignalFields.q2
  q3: bool = AlarmSignalFields.q3
  q4: bool = AlarmSignalFields.q4
  q5: bool = AlarmSignalFields.q5
  q6: bool = AlarmSignalFields.q6

