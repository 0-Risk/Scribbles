from django.contrib.auth import get_user_model
import graphene
from scribbles.apps.authentication.schema.queries.users_query import UserType


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:

        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String()

    def mutate(self, info, username, email, password):
        user = get_user_model()(username=username, email=email, password=password)
        user.set_password(password)
        user.save()
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
