from .models import Ticket as TicketModel
from graphene_django import DjangoObjectType
import graphene


class ticket(DjangoObjectType):
    class Meta:
        model = TicketModel


class Query(graphene.ObjectType):
    users = graphene.List(ticket)

    def resolve_ticket(self, info):
        return TicketModel.objects.all()
