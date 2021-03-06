"""MODELS - FIELDS
Definition of Fields used on model classes attributes.
We define them separately because the PersonUpdate and PersonCreate models need to re-define their attributes,
as they change from Optional to required.
Address could define its fields on the model itself, but we define them here for convenience
"""

# # Installed # #
from pydantic import Field

# # Package # #
from ..utils import get_time, get_uuid

__all__ = ("ContactFields", "AddressFields", "ComorbidityFields",
           "SymptomFields")

_string = dict(min_length=1)
"""Common attributes for all String fields"""
_unix_ts = dict(example=get_time())
"""Common attributes for all Unix timestamp fields"""


class ContactFields:
    name = Field(description="Name of this person", example="John", **_string)
    first_name = Field(description="First name of this person",
                       example="Doe",
                       **_string)
    last_name = Field(description="Last name of this person",
                      example="Smith",)

    doc_type = Field(description="Document type of this person",
                     example="DNI",
                     **_string)
    doc_number = Field(description="Document number of this person",
                       example="45117789",
                       **_string)
    address = Field(description="Address object where this person live")
    address_update = Field(
        description=f"{address.description}. When updating, the whole Address object is required, as it gets replaced"
    )
    comorbidities = Field(description="Comorbidity object")
    comorbidities_update = Field(
        description=f"{comorbidities.description}. When updating, the whole Comorbidity object is required, as it gets replaced"
    )
    symptoms = Field(description="Symptoms object")
    symptoms_update = Field(
        description=f"{symptoms.description}. When updating, the whole Symptoms object is required, as it gets replaced"
    )
    birth = Field(
        description="Date of birth, in format YYYY-MM-DD, or Unix timestamp",
        example="1999-12-31")
    start_date = Field(
        description="Symptom register start date, in format YYYY-MM-DD, or Unix timestamp",
        example="2021-10-04")
    age = Field(
        description="Age of this person, if date of birth is specified",
        example=20)
    alternative_cellphone_number = Field(description="Alternative Cellphone number of this person",
                         example=935397346)
    cellphone_number = Field(description="Cellphone number of this person",
                             example=935397346)
    person_id = Field(
        description="Unique identifier of this person in the database",
        example=get_uuid(),
        min_length=36,
        max_length=36)
    """The person_id is the _id field of Mongo documents, and is set on PeopleRepository.create"""

    created = Field(
        alias="created",
        description="When the person was registered (Unix timestamp)",
        **_unix_ts)
    """Created is set on PeopleRepository.create"""
    updated = Field(
        alias="updated",
        description="When the person was updated for the last time (Unix timestamp)",
        **_unix_ts)
    """Created is set on PeopleRepository.update (and initially on create)"""


class AddressFields:
    street = Field(description="Main address line",
                   example="22nd Bunker Hill Avenue",
                   **_string)
    city = Field(description="City", example="Hamburg - PER", **_string)
    state = Field(description="State, province and/or region",
                  example="Mordor",
                  **_string)
    zip_code = Field(description="Postal/ZIP code", example="19823", **_string)


class ComorbidityFields:
    q1 = Field(description="Enfermedad cardiovascular", example=True)
    q2 = Field(description="Enfermedad renal cr??nica", example=True)
    q3 = Field(description="Enfermedad respiratoria cr??nica", example=True)
    q4 = Field(description="Enfermedad hep??tica cr??nica", example=True)
    q5 = Field(description="Diabetes", example=True)
    q6 = Field(description="C??ncer", example=True)
    q7 = Field(description="VIH", example=True)
    q8 = Field(description="Tuberculosis activa", example=True)
    q9 = Field(description="Transtornos neurol??gicos cr??nicos", example=True)
    q10 = Field(description="Transtornos de c??lulas falciformes", example=True)
    q11 = Field(description="Consumo de tabaco", example=True)
    q12 = Field(description="Obecidad severa (IMC > 40)", example=True)
    q13 = Field(description="Hipertensi??n", example=True)
    q14 = Field(description="Gestante", example=True)
    q15 = Field(description="Mayor de 60 a??os", example=True)
    q16 = Field(description="Personal de salud", example=True)
    created = Field(
        alias="created",
        description="When the comorbidity was registered (Unix timestamp)",
        **_unix_ts)
    updated = Field(
        alias="updated",
        description="When the comorbidity was updated for the last time (Unix timestamp)",
        **_unix_ts)


class EessFields:
    code = Field(description="C??digo del establecimiento de salud",
                 example="01",
                 **_string)
    name = Field(description="Nombre del establecimiento de salud",
                 example="AMAZONAS",
                 **_string)


class DepartmentFields:
    code = Field(description="C??digo", example="01", **_string)
    name = Field(description="Nombre", example="AMAZONAS", **_string)


class SymptomFields:
    person_id = Field(
        description="Id de la persona",
        example="62c64bab-1f44-49dc-9ba3-6af33c887a12",
        **_string,
    )
    symptom_id = Field(description="Id de la s??ntoma",
                       example="c7166343-0913-4dc2-91e5-569d7d66f905",
                       **_string)
    q1 = Field(description="Tos y/o dolor de garganta", example=True)
    q1 = Field(description="Tos y/o dolor de garganta", example=True)
    q2 = Field(description="Malestar general", example=True)
    q3 = Field(description="Fiebre > 38??C", example=True)
    q4 = Field(description="Cefalea", example=True)
    q5 = Field(description="Congesti??n nasal", example=True)
    q6 = Field(description="Diarrea", example=True)
    q7 = Field(description="Dificultad para respirar", example=True)
    q8 = Field(description="P??rdida de olfato (Anosmia)", example=True)
    q9 = Field(description="P??rdida de gusto (Ageusia)", example=True)
    q10 = Field(description="Otro (describir)", example="Otro", **_string)
    is_suspicious = Field(description="??Es sospechoso?", example=True)
    latitude = Field(description="Latitud", example="12.123123", **_string)
    longitude = Field(description="Longitud", example="12.123123", **_string)
    alarm_signal = Field(description="Signos de alarma", **_string)
    created_at = Field(
        alias="created",
        description="When the Symptoms was registered (Unix timestamp)",
        **_unix_ts)
    updated_at = Field(
        alias="updated",
        description="When the symptoms was updated for the last time (Unix timestamp)",
        **_unix_ts)

class AlarmSignalFields:
    q1 = Field(description="Disnea", example=True)
    q2 = Field(description="Taquipedia (>=22 rpm)", example=True)
    q3 = Field(description="Saturaci??n de ox??geno < 92%", example=True)
    q4 = Field(description="Alteraci??n de la conciencia", example=True)
    q5 = Field(description="Otro signo", example=True)
    q6 = Field(description="Ninguno", example=True)