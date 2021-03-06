from django.urls import path
from .views import IndexView, ContatoView, PostDetailView, SobreView, SearchResultsView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('detail/<int:id>', PostDetailView.as_view(), name='detail'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('search/', SearchResultsView.as_view(), name='search_results' ),
]