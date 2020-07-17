from django.urls import path

from . import views
# from .views import (UserTodoListView)
#                    AddTodo,
#                    CompleteTodo,
#                    DeleteCompleted,
#                    DeleteAll)

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall')
    # path('user/<str:username>',UserTodoListView.as_view(), name = 'user-todos'),
    # path('add',AddTodo.as_view(), name = 'add'),
    # path('user/<str:username>/<int:todo_id>',CompleteTodo.as_view(), name = 'complete'),
    # path('user/<str:username>',DeleteCompleted.as_view(), name = 'deletecomplete'),
    # path('user/<str:username>',DeleteAll.as_view(), name = 'deleteall'),
    # path('add', views.addTodo, name='add'),
    # path('complete/<todo_id>', views.completeTodo, name='complete'),
    # path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    # path('deleteall', views.deleteAll, name='deleteall')
]
