from django.urls import path

from bookmark.views import BookmarkList, BookmarkCreateView, BookmarkDetailView

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkList.as_view(), name='list'),  # {% url 'bookmark:list' %}
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail') #집에가고싶다... 커밋이안되니까주석이라도 써본다
]
