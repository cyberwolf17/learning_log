from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^users/', include(('users.urls', 'users'), namespace='users')),
    url(r'', include(('learning_logs.urls', 'learning_logs'), namespace='learning_logs')),
]
