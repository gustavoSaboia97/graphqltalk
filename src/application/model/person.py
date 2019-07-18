from graphene import ObjectType
import graphene


class Person(ObjectType):

    id = graphene.String()
    name = graphene.String()
    age = graphene.Int()
    nickname = graphene.String()
    best_friend = graphene.String()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "nickname": self.nickname,
            "best_friend": self.best_friend
        }

    def to_mongo_dict(self) -> dict:
        return {
            "name": self.name,
            "age": self.age,
            "nickname": self.nickname,
            "best_friend": self.best_friend
        }
