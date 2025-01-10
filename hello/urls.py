from django.urls import path
from . import views
from graphene_django.views import GraphQLView

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]