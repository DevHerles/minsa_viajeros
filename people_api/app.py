"""APP
FastAPI app definition, initialization and definition of routes
"""

# # Installed # #
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status as statuscode

# # Package # #
from .models import *
from .exceptions import *
from .repositories import PeopleRepository, SymptomsRepository
from .middlewares import request_handler
from .settings import api_settings as settings

__all__ = ("app", "run")

app = FastAPI(title=settings.title)
app.middleware("http")(request_handler)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
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
         response_model=PersonRead,
         description="Get a single person by its unique IMEI",
         responses=get_exception_responses(PersonNotFoundException),
         tags=["people"])
def _get_person(imei: str):
    return PeopleRepository.getByImei(imei)


@app.get("/people",
         response_model=PeopleRead,
         description="List all the available persons",
         tags=["people"])
def _list_people():
    # TODO Filters
    return PeopleRepository.list()


@app.get("/people/{person_id}",
         response_model=PersonRead,
         description="Get a single person by its unique ID",
         responses=get_exception_responses(PersonNotFoundException),
         tags=["people"])
def _get_person(person_id: str):
    return PeopleRepository.get(person_id)


@app.post("/people",
          description="Create a new person",
          response_model=PersonRead,
          status_code=statuscode.HTTP_201_CREATED,
          responses=get_exception_responses(PersonAlreadyExistsException),
          tags=["people"])
def _create_person(create: PersonCreate):
    return PeopleRepository.create(create)


@app.patch(
    "/people/{person_id}",
    description="Update a single person by its unique ID, providing the fields to update",
    status_code=statuscode.HTTP_204_NO_CONTENT,
    responses=get_exception_responses(PersonNotFoundException,
                                      PersonAlreadyExistsException),
    tags=["people"])
def _update_person(person_id: str, update: PersonUpdate):
    PeopleRepository.update(person_id, update)


# Symtoms


@app.get("/person-symptoms/{person_id}",
         response_model=SymptomsRead,
         description="List all the available symptoms",
         tags=["symptoms"])
def _list_person_symptoms(person_id: str):
    # TODO Filters
    print(person_id)
    return SymptomsRepository.list(person_id)


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
            responses=get_exception_responses(PersonNotFoundException),
            tags=["people"])
def _delete_person(person_id: str):
    PeopleRepository.delete(person_id)


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(app,
                host=settings.host,
                port=settings.port,
                log_level=settings.log_level.lower())
