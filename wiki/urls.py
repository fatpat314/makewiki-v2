from django.urls import path
from wiki.views import PageListView, PageDetailView, New_wiki_form


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('form/', New_wiki_form.as_view(), name='new'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('form/', New_wiki_form.as_view(), name='new')
]
