from .models import Account as UserModel
import graphene
from graphene_django import DjangoObjectType


# from django.db.models import Q   #for advanced OR Querying, not needed
# from graphql import GraphQLError


class User(DjangoObjectType):
    class Meta:
        model = UserModel


class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return UserModel.objects.all()


# Mutations

class AddUser(graphene.Mutation):
    user_id = graphene.ID()

    class Arguments:
        username = graphene.String()
        password = graphene.String()
        email = graphene.String()
        # Actually going to be a byte array converted to a string and sent over

    def mutate(self, info, username, email, password):
        user = UserModel(username=username, password=password, email=email)
        user.save()
        return AddUser(user_id=user.id)


# class UpdateUser(graphene.Mutation):
#     success = graphene.Boolean()
#
#     class Arguments:
#         user_id = graphene.Int()
#         name = graphene.String()
#         is_admin = graphene.Boolean()
#         password = graphene.String()
#         points = graphene.Int()
#         avatar = graphene.String()
#
#     def mutate(self, info, user_id, name, is_admin, points, password = None, avatar = None):
#         user = User.objects.get(id = user_id)
#
#         user.name = name
#         user.is_admin = is_admin
#         user.points = points
#         if is_admin == True:
#             if password == None:
#                 raise GraphQLError("Is Admin, but no password was provided")
#             user.password = password
#         if avatar != None:
#             user.avatar = avatar
#
#         user.save()
#
#         return UpdateUser(success = True)

class DeleteUser(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        user_id = graphene.ID()

    def mutate(self, info, user_id):
        user = UserModel.objects.get(id=user_id)
        user.delete()

        # may have to end up going and deleting all owned chores to keep DB happy, not sure yet.
        # DB handler doesn't seem to have to though.

        return DeleteUser(success=True)


class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()
    delete_user = DeleteUser.Field()
