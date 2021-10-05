"""APP
FastAPI app definition, initialization and definition of routes
"""

# # Installed # #
from people_api.models.alarm_signal_create import AlarmSignalCreate
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status as statuscode
from fastapi.responses import JSONResponse

# # Package # #
from .models import *
from .exceptions import *
from .repositories import ContactRepository, SymptomsRepository
from .middlewares import request_handler
from .settings import api_settings as settings

__all__ = ("app", "run")

app = FastAPI(title=settings.title)
app.middleware("http")(request_handler)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/imei/{imei}",
         response_model=ContactRead,
         description="Get a single person by its unique IMEI",
         responses=get_exception_responses(ContactNotFoundException),
         tags=["people"])
def _get_contact(imei: str):
    return ContactRepository.getByImei(imei)


@app.get("/people",
         response_model=ContactsRead,
         description="List all the available persons",
         tags=["people"])
def _list_contacts():
    # TODO Filters
    return ContactRepository.list()


@app.get("/people/{contact_id}",
         response_model=ContactRead,
         description="Get a single person by its unique ID",
         responses=get_exception_responses(ContactNotFoundException),
         tags=["people"])
def _get_contact(contact_id: str):
    return ContactRepository.get(contact_id)


@app.post("/people",
          description="Create a new person",
          response_model=ContactRead,
          status_code=statuscode.HTTP_201_CREATED,
          responses=get_exception_responses(ContactAlreadyExistsException),
          tags=["people"])
def _create_person(create: ContactCreate):
    print(create)
    return ContactRepository.create(create)


@app.patch(
    "/people/{contact_id}",
    description="Update a single person by its unique ID, providing the fields to update",
    status_code=statuscode.HTTP_204_NO_CONTENT,
    responses=get_exception_responses(ContactNotFoundException,
                                      ContactAlreadyExistsException),
    tags=["people"])
def _update_contact(contact_id: str, update: ContactUpdate):
    ContactRepository.update(contact_id, update)


@app.patch(
    "/people-symptom/{contact_id}",
    description="Add a single symptom object for person by its unique ID, providing the fields to update",
    status_code=statuscode.HTTP_204_NO_CONTENT,
    responses=get_exception_responses(ContactNotFoundException,
                                      ContactAlreadyExistsException),
    tags=["people"])
def _add_symptom(contact_id: str, update: SymptomUpdate):
    ContactRepository.addSymptom(contact_id, update)

@app.patch(
    "/people-symptom-alarmsignal/{contact_id}",
    description="Add a single symptom object for person by its unique ID, providing the fields to update",
    status_code=statuscode.HTTP_204_NO_CONTENT,
    responses=get_exception_responses(ContactNotFoundException,
                                      ContactAlreadyExistsException),
    tags=["people"])
def _add_alarmsignal(contact_id: str, update: AlarmSignalCreate):
    ContactRepository.addAlarmSignal(contact_id, update)


# Symtoms


@app.get("/person-symptoms/{person_id}",
         response_model=SymptomsRead,
         description="List all the available symptoms",
         tags=["symptoms"])
def _list_person_symptoms(contact_id: str):
    # TODO Filters
    print(contact_id)
    return SymptomsRepository.list(contact_id)


@app.get("/symptoms",
         response_model=SymptomsRead,
         description="List all the available symptoms",
         tags=["symptoms"])
def _list_symptoms():
    # TODO Filters
    return SymptomsRepository.list()


@app.get("/symptoms/{symptom_id}",
         response_model=SymptomRead,
         description="Get a single symptom by its unique ID",
         responses=get_exception_responses(SymptomNotFoundException),
         tags=["symptoms"])
def _get_symptom(symptom_id: str):
    return SymptomRepository.get(symptom_id)


@app.post("/symptoms",
          description="Create a new symptom",
          response_model=SymptomRead,
          status_code=statuscode.HTTP_201_CREATED,
          responses=get_exception_responses(SymptomAlreadyExistsException),
          tags=["symptoms"])
def _create_symptom(create: SymptomCreate):
    return SymptomsRepository.create(create)


@app.patch(
    "/symptoms/{symptoms_id}",
    description="Update a single symptom by its unique ID, providing the fields to update",
    status_code=statuscode.HTTP_204_NO_CONTENT,
    responses=get_exception_responses(SymptomNotFoundException,
                                      SymptomAlreadyExistsException),
    tags=["symptoms"])
def _update_symptom(symptom_id: str, update: SymptomUpdate):
    SymptomRepository.update(symptom_id, update)


@app.delete("/symptoms/{symptom_id}",
            description="Delete a single symptom by its unique ID",
            status_code=statuscode.HTTP_204_NO_CONTENT,
            responses=get_exception_responses(SymptomNotFoundException),
            tags=["symptoms"])
def _delete_symptom(symptom_id: str):
    SymptomsRepository.delete(symptom_id)


@app.delete("/people/{person_id}",
            description="Delete a single person by its unique ID",
            status_code=statuscode.HTTP_204_NO_CONTENT,
            responses=get_exception_responses(ContactNotFoundException),
            tags=["people"])
def _delete_person(contact_id: str):
    ContactRepository.delete(contact_id)


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(app,
                host=settings.host,
                port=settings.port,
                log_level=settings.log_level.lower())
