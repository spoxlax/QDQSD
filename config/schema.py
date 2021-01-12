import graphene
import account.schema
import ticket.schema


class Query(
    account.schema.Query,
    ticket.schema.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    account.schema.Mutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
