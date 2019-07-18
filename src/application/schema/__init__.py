from .querys import Query
from .mutations import MyMutations
import graphene


schema = graphene.Schema(query=Query, mutation=MyMutations)
