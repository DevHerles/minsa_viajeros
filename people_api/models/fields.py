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

__all__ = ("PersonFields", "AddressFields", "ComorbidityFields",
           "SymptomFields")

_string = dict(min_length=1)
"""Common attributes for all String fields"""
_unix_ts = dict(example=get_time())
"""Common attributes for all Unix timestamp fields"""


class PersonFields:
    name = Field(description="Name of this person", example="John", **_string)
    first_name = Field(description="First name of this person",
                       example="Doe",
                       **_string)
    last_name = Field(description="Last name of this person",
                      example="Smith",
                      **_string)

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
    age = Field(
        description="Age of this person, if date of birth is specified",
        example=20)
    phone_number = Field(description="Phone number of this person",
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
    q1 = Field(description="Enfermedad cardiovascular",
               example="SI",
               **_string)
    q2 = Field(description="Enfermedad renal crónica", example="SI", **_string)
    q3 = Field(description="Enfermedad respiratoria crónica",
               example="SI",
               **_string)
    q4 = Field(description="Enfermedad hepática crónica",
               example="SI",
               **_string)
    q5 = Field(description="Diabetes", example="SI", **_string)
    q6 = Field(description="Cáncer", example="SI", **_string)
    q7 = Field(description="VIH", example="SI", **_string)
    q8 = Field(description="Tuberculosis activa", example="SI", **_string)
    q9 = Field(description="Transtornos neurológicos crónicos",
               example="SI",
               **_string)
    q10 = Field(description="Transtornos de células falciformes",
                example="SI",
                **_string)
    q11 = Field(description="Consumo de tabaco", example="SI", **_string)
    q12 = Field(description="Obecidad severa (IMC > 40)",
                example="SI",
                **_string)
    q13 = Field(description="Hipertensión", example="SI", **_string)
    q14 = Field(description="Gestante", example="SI", **_string)
    q15 = Field(description="Mayor de 60 años", example="SI", **_string)
    q16 = Field(description="Personal de salud", example="SI", **_string)
    created = Field(
        alias="created",
        description="When the comorbidity was registered (Unix timestamp)",
        **_unix_ts)
    updated = Field(
        alias="updated",
        description="When the comorbidity was updated for the last time (Unix timestamp)",
        **_unix_ts)


class SymptomFields:
    person_id = Field(
        description="Id de la persona",
        example="62c64bab-1f44-49dc-9ba3-6af33c887a12",
        **_string,
    )
    symptom_id = Field(description="Id de la síntoma",
                       example="c7166343-0913-4dc2-91e5-569d7d66f905",
                       **_string)
    q1 = Field(description="Tos y/o dolor de garganta",
               example="SI",
               **_string)
    q1 = Field(description="Tos y/o dolor de garganta",
               example="SI",
               **_string)
    q2 = Field(description="Malestar general", example="SI", **_string)
    q3 = Field(description="Fiebre > 38ºC", example="SI", **_string)
    q4 = Field(description="Cefalea", example="SI", **_string)
    q5 = Field(description="Congestión nasal", example="SI", **_string)
    q6 = Field(description="Diarrea", example="SI", **_string)
    q7 = Field(description="Dificultad para respirar", example="SI", **_string)
    q8 = Field(description="Pérdida de olfato (Anosmia)",
               example="SI",
               **_string)
    q9 = Field(description="Pérdida de gusto (Ageusia)",
               example="SI",
               **_string)
    q10 = Field(description="Otro (describir)", example="Otro", **_string)
    latitude = Field(description="Latitud", example="12.123123", **_string)
    longitude = Field(description="Longitud", example="12.123123", **_string)
    created = Field(
        alias="created",
        description="When the Symptoms was registered (Unix timestamp)",
        **_unix_ts)
    updated = Field(
        alias="updated",
        description="When the symptoms was updated for the last time (Unix timestamp)",
        **_unix_ts)
