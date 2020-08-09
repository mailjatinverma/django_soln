import graphene
import sts.schema


class Query(sts.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as and when we begin to add more apps to our project
    pass


class Mutation(sts.schema.Mutation, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as and when we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)