from django.urls import path
from django.urls import re_path

from apps.manager import views
from .views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerLicenseUpdateView,
    WorkerDeleteView,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    toggle_assign_to_task, PositionListView, PositionCreateView, PositionUpdateView, PositionDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "tasktypes/",
        TaskTypeListView.as_view(),
        name="tasktype-list",
    ),
    path(
        "tasktypes/create/",
        TaskTypeCreateView.as_view(),
        name="tasktype-create",
    ),
    path(
        "tasktypes/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="tasktype-update",
    ),
    path(
        "tasktypes/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="tasktype-delete",
    ),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "tasks/<int:pk>/toggle-assign/",
        toggle_assign_to_task,
        name="toggle-task-assign",
    ),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path(
        "workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"
    ),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path(
        "workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"
    ),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path(
        "workers/<int:pk>/update/",
        WorkerLicenseUpdateView.as_view(),
        name="worker-update",
    ),
    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete",
    ),
    path(
        "position/",
        PositionListView.as_view(),
        name="position-list",
    ),
    path(
        "positions/create/",
        PositionCreateView.as_view(),
        name="position-create",
    ),
    path(
        "positions/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "positions/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete",
    ),
    re_path(r'^.*\.*', views.pages, name='pages')
]

app_name = "manager"
