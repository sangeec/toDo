from django.urls import path
from . import views

urlpatterns = [
    # Add Task
    path('addTask/', views.addTask, name='addTask'),
    # Mark as complete
    path('mark_as_done/<int:taskId>', views.mark_as_done, name='mark_as_complete'),
    #Edit Functionality
    path('edit_task/<int:taskId>', views.edit_task, name='modify_Task_Name'),
    #Delete Functionality
    path('delete_task/<int:taskId>', views.delete_task, name='delete_Task_Name'),
    # Mark as incomplete
    path('mark_as_undone/<int:taskId>', views.mark_as_undone, name='mark_as_incomplete'),
]