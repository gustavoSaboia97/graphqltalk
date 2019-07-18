from src.settings.mongo_connection import database
from src.application.model.person import Person
from src.util.logger import get_logger

log = get_logger()


class PersonRepo:

    def __init__(self):
        self.__person_collection = database.person_collection

    def add_new_person(self, person: Person) -> Person:
        log.info(f"Inserting new user: {person.name}")

        person_mongo_object = self.__person_collection.insert_one(person.to_mongo_dict())
        person_id = person_mongo_object.inserted_id

        person.id = str(person_id)

        return person

    def get_persons(self) -> list:
        log.info("Getting persons")

        persons = list()

        for person_document in self.__person_collection.find():
            person = Person()

            person.id = str(person_document['_id'])
            person.name = str(person_document['name'])
            person.nickname = str(person_document['nickname'])
            person.age = str(person_document['age'])
            person.best_friend = str(person_document['best_friend'])

            persons.append(person)

        return persons

    def get_person_by_nickname(self, nickname: str) -> Person:
        log.info(f"Getting user by nickname: {nickname}")

        person = None

        for person_document in self.__person_collection.find({"nickname": nickname}):
            person = Person()

            person.id = str(person_document['_id'])
            person.name = str(person_document['name'])
            person.nickname = str(person_document['nickname'])
            person.age = str(person_document['age'])
            person.best_friend = str(person_document['best_friend'])

        return person
