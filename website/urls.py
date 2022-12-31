from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings
from .settings import MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blogs, name='blog'),
    path('tambah/<int:id_baru>', Data_baru, name='Data_baru'),
    path('blog/ubah/<int:id_data>', ubah_data, name='ubah_data'),
    path('blog/hapus/<int:id_data>', hapus_data, name='hapus_data'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
