from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'node', views.nodeView)
router.register(r'graph', views.graphView)
router.register(r'activesubgraph', views.activesubgraphView)
router.register(r'emoji', views.emojiView)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]