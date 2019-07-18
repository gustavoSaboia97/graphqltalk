from src.application.repository import PersonRepo
from src.application.model import Person
from graphene import ObjectType
import graphene


class Query(ObjectType):
    person = graphene.Field(Person, nickname=graphene.String(required=True))
    persons = graphene.List(Person)

    def resolve_person(self, info, nickname: str) -> Person:

        repo = PersonRepo()
        person_info = repo.get_person_by_nickname(nickname)

        if person_info is None:
            return None

        return Person(
            id=person_info.id,
            name=person_info.name,
            age=person_info.age,
            nickname=person_info.nickname,
            best_friend=person_info.best_friend
        )

    def resolve_persons(self, info) -> list:

        repo = PersonRepo()
        return repo.get_persons()
