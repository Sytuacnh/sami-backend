"""sami URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

# from programs.views import ProgramsViewSet
from users.views import UsersViewSet
from contactmessages.views import ContactMessagesViewSet

# for static
from django.conf import settings
from django.conf.urls.static import static

# xadmin
import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()

router = DefaultRouter()

# /api/programs -> ProgramsViewSet
# router.register(r'programs', ProgramsViewSet) # doesn't need to add base_name="programs"
router.register(r'contactmessages', ContactMessagesViewSet)
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api/', include(router.urls)),

    # login URLs for the browsable API. able to login 
    path('api-login/', include('rest_framework.urls', namespace='rest_framework')),
    # api doc
    path('docs/', include_docs_urls(title="SAMI")),
# ]
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)