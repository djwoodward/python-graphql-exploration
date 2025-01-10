from django.urls import path
from . import views
from graphene_django.views import GraphQLView

urlpatterns = [
    path('', views.app_world, name='app_world'),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]