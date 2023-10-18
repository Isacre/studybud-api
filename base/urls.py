from rest_framework.routers import DefaultRouter
from base.views.rooms import RoomsViewset
from base.views.messages import MessagesViewset
from base.views.topic import TopicViewset
from base.views.user import UserViewset



router = DefaultRouter()
router.register(r'users', UserViewset, basename='user')
router.register(r'topics', TopicViewset, basename='topic')
router.register(r'rooms', RoomsViewset, basename='room')
router.register(r'messages', MessagesViewset, basename='message')


urlpatterns = router.urls
