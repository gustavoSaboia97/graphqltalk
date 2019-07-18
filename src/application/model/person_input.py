from graphene import InputObjectType
import graphene


class PersonInput(InputObjectType):

    id = graphene.String()
    name = graphene.String()
    age = graphene.Int()
    nickname = graphene.String()
    best_friend = graphene.String()
