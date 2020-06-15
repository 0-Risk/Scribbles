import graphene
import graphql_jwt
from scribbles.apps.authentication.schema.mutations import create_user_mutation as schema_mutation
from scribbles.apps.authentication.schema.queries import users_query as schema_query


class Query(schema_query.Query, graphene.ObjectType):
    pass


class Mutation(schema_mutation.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
