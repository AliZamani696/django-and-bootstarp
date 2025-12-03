
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include("django.contrib.auth.urls")),
    path('',views.Home.as_view()),
    path('store/', include( "Store.urls")),
    path('accounts/', include( "Accounts.urls")),
    path('cart/', include( "Cart.urls")),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




urlpatterns += [
    path('<path:unmatched>', views.NotFoundView.as_view(), name='catch-all'),
]