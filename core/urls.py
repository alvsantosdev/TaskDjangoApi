from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FuncionarioViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'tarefas', TaskViewSet)

urlpatterns = [

    path('', include(router.urls)),
]