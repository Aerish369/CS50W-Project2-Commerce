from django.urls import path

#! for image upload routing
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    #! Crud of the listings
    path('create-listing', views.createListing, name='create-listing'),
    path('listing/<int:pk>/', views.bidListing, name='listing'),
    path('close-listing/<int:pk>/', views.closeListing, name='close-listing'),

    #! Watchlist
    path('watchlist/<int:pk>/', views.addRemoveWatchlist, name='watchlist'),
    path('watchlist/', views.viewWatchlist, name='view-watchlist'),

    path('comment/<int:pk>/', views.addComment, name='comment'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    