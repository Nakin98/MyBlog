from django.urls import path
from . import views
urlpatterns = [

    path('', views.HomeView.as_view(paginate_by = 5), name ='homepage' ),
    path('crea_post/',views.crea_post, name='crea_post'),
    path('post/<int:pk>', views.post, name='post_singolo'),
    path('cerca/', views.cerca, name='funzione_cerca'),
]
