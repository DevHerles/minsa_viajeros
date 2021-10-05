"""REPOSITORIES
Methods to interact with the database
"""

# # Package # #
from people_api.models.alarm_signal_create import AlarmSignalCreate
from .models import *
from .exceptions import *
from .database import collection, symptomCollection
from .utils import get_time, get_uuid

__all__ = (
    "ContactRepository",
    "SymptomsRepository",
)


class ContactRepository:
    @staticmethod
    def getByImei(imei: str) -> ContactRead:
        """Retrieve a single Person by its unique IMEI"""
        print(imei)
        document = collection.find_one({"imei": imei})
        if not document:
            raise ContactNotFoundException(imei)
        return ContactRead(**document)

    @staticmethod
    def get(contact_id: str) -> ContactRead:
        """Retrieve a single Person by its unique id"""
        document = collection.find_one({"_id": contact_id})
        print(document)
        if not document:
            raise ContactNotFoundException(contact_id)
        return ContactRead(**document)

    @staticmethod
    def list() -> ContactsRead:
        """Retrieve all the available persons"""
        cursor = collection.find()
        # for document in cursor:
        #     print(document)
        return [ContactRead(**document) for document in cursor]

    @staticmethod
    def create(create: ContactCreate) -> ContactRead:
        """Create a person and return its Read object"""
        print(create)
        document = create.dict()
        document["created"] = document["updated"] = get_time()
        document["_id"] = get_uuid()
        # The time and id could be inserted as a model's Field default factory,
        # but would require having another model for Repository only to implement it

        result = collection.insert_one(document)
        assert result.acknowledged

        return ContactRepository.get(result.inserted_id)

    @staticmethod
    def update(contact_id: str, update: ContactUpdate):
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
        result = collection.update_one({"_id": contact_id}, {"$set": document})
        if not result.modified_count:
            raise ContactNotFoundException(identifier=contact_id)

    @staticmethod
    def addSymptom(contact_id: str, update: SymptomUpdate):
        """Add a person symptom by giving only the fields to update"""
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
        result = collection.update_one({"_id": contact_id},
                                       {"$push": {
                                           "symptoms": document
                                       }})
        if not result.modified_count:
            raise ContactNotFoundException(identifier=contact_id)

    @staticmethod
    def addAlarmSignal(contact_id: str, update: AlarmSignalCreate):
        """Add a person symptom by giving only the fields to update"""
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
        result = collection.update_one({"_id": contact_id},
                                       {"$set": {
                                           "symptoms.alarm_signal": document
                                       }})
        if not result.modified_count:
            raise ContactNotFoundException(identifier=contact_id)

    @staticmethod
    def delete(contact_id: str):
        """Delete a person given its unique id"""
        result = collection.delete_one({"_id": contact_id})
        if not result.deleted_count:
            raise ContactNotFoundException(identifier=contact_id)


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
