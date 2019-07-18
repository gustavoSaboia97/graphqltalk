from src.application.repository import PersonRepo
from src.application.model import PersonInput, Person
from graphene import Mutation, ObjectType
import graphene


class CreatePerson(Mutation):

    class Arguments:
        person_data = PersonInput(required=True)

    person = graphene.Field(Person)

    def mutate(self, info, person_data=None):

        created_person = Person()

        created_person.name = person_data.name
        created_person.age = person_data.age
        created_person.nickname = person_data.nickname
        created_person.best_friend = person_data.best_friend

        repo = PersonRepo()

        created_person = repo.add_new_person(created_person)

        return CreatePerson(person=created_person)


class MyMutations(ObjectType):
    create_person = CreatePerson.Field()
