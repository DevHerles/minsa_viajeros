"""REPOSITORIES
Methods to interact with the database
"""

# # Package # #
from .models import *
from .exceptions import *
from .database import collection, symptomCollection
from .utils import get_time, get_uuid

__all__ = (
    "PeopleRepository",
    "SymptomsRepository",
)


class PeopleRepository:
    @staticmethod
    def getByImei(imei: str) -> PersonRead:
        """Retrieve a single Person by its unique IMEI"""
        print(imei)
        document = collection.find_one({"imei": imei})
        if not document:
            raise PersonNotFoundException(imei)
        return PersonRead(**document)

    @staticmethod
    def get(person_id: str) -> PersonRead:
        """Retrieve a single Person by its unique id"""
        document = collection.find_one({"_id": person_id})
        if not document:
            raise PersonNotFoundException(person_id)
        return PersonRead(**document)

    @staticmethod
    def list() -> PeopleRead:
        """Retrieve all the available persons"""
        cursor = collection.find()
        return [PersonRead(**document) for document in cursor]

    @staticmethod
    def create(create: PersonCreate) -> PersonRead:
        """Create a person and return its Read object"""
        print(create)
        document = create.dict()
        document["created"] = document["updated"] = get_time()
        document["_id"] = get_uuid()
        # The time and id could be inserted as a model's Field default factory,
        # but would require having another model for Repository only to implement it

        result = collection.insert_one(document)
        assert result.acknowledged

        return PeopleRepository.get(result.inserted_id)

    @staticmethod
    def update(person_id: str, update: PersonUpdate):
        """Update a person by giving only the fields to update"""
        # record = collection.find_one({"_id": person_id})
        # if not record:
        #     raise PersonNotFoundException(person_id)
        document = update.dict()
        document["updated"] = get_time()
        # symptoms = record.pop("symptoms")
        # print(symptoms)
        # symptoms.append(document)
        # document["symptoms"] = symptoms
        # print(document)
        result = collection.update_one({"_id": person_id}, {"$set": document})
        if not result.modified_count:
            raise PersonNotFoundException(identifier=person_id)

    @staticmethod
    def delete(person_id: str):
        """Delete a person given its unique id"""
        result = collection.delete_one({"_id": person_id})
        if not result.deleted_count:
            raise PersonNotFoundException(identifier=person_id)


class SymptomsRepository:
    @staticmethod
    def get(symptom_id: str) -> SymptomRead:
        """Retrieve a single Symptom by its unique id"""
        document = symptomCollection.find_one({"_id": symptom_id})
        if not document:
            raise SymptomNotFoundException(symptom_id)
        return SymptomRead(**document)

    @staticmethod
    def list(person_id: str) -> SymptomsRead:
        """Retrieve all the available symptoms"""
        print("person_id", person_id)
        cursor = symptomCollection.find({"person_id": person_id})
        return [SymptomRead(**document) for document in cursor]

    @staticmethod
    def create(create: SymptomCreate) -> SymptomRead:
        """Create a symptom and return its Read object"""
        document = create.dict()
        document["created"] = document["updated"] = get_time()
        document["_id"] = get_uuid()
        # The time and id could be inserted as a model's Field default factory,
        # but would require having another model for Repository only to implement it

        result = symptomCollection.insert_one(document)
        assert result.acknowledged

        return SymptomsRepository.get(result.inserted_id)

    @staticmethod
    def update(symptom_id: str, update: SymptomUpdate):
        """Update a symptom by giving only the fields to update"""
        # record = collection.find_one({"_id": person_id})
        # if not record:
        #     raise PersonNotFoundException(person_id)
        document = update.dict()
        document["updated"] = get_time()
        # symptoms = record.pop("symptoms")
        # print(symptoms)
        # symptoms.append(document)
        # document["symptoms"] = symptoms
        # print(document)
        result = symptomCollection.update_one({"_id": symptom_id},
                                              {"$set": document})
        if not result.modified_count:
            raise SymptomNotFoundException(identifier=symptom_id)

    @staticmethod
    def delete(symptom_id: str):
        """Delete a symptom given its unique id"""
        result = symptomCollection.delete_one({"_id": symptom_id})
        if not result.deleted_count:
            raise SymptomNotFoundException(identifier=symptom_id)


# class ComorbidityRespository:
#     @staticmethod
#     def create(create: ComorbidityCreate) -> ComorbidityCreate:
#         """Create a comorbidity and return its Read object"""
#         document = create.dict()
#         document["created"] = document["updated"] = get_time()
#         document["_id"] = get_uuid()
#         result = collection.insert_one(document)
#         assert result.acknowledged

#         return result

# class SymptomsRepository:
#     @staticmethod
#     def create(create: SymptomsCreate) -> SymptomsCreate:
#         """Create a symptoms and return its Read object"""
#         document = create.dict()
#         document["created"] = document["updated"] = get_time()
#         document["_id"] = get_uuid()
#         result = collection.insert_one(document)
#         assert result.acknowledged

#         return result
