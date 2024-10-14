from django.contrib import admin
from django.urls import path
from dogapi.views import DogViewSet, BreedViewSet
from rest_framework.urlpatterns import format_suffix_patterns

# Instantiate the viewsets
dog_list = DogViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

dog_detail = DogViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

breed_list = BreedViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

breed_detail = BreedViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL

    # Dog endpoints
    path('api/dogs/', dog_list, name='dog-list-create'),  # List all dogs or create a new dog
    path('api/dogs/<int:pk>/', dog_detail, name='dog-detail'),  # Retrieve, update, or delete a specific dog

    # Breed endpoints
    path('api/breeds/', breed_list, name='breed-list-create'),  # List all breeds or create a new breed
    path('api/breeds/<int:pk>/', breed_detail, name='breed-detail'),  # Retrieve, update, or delete a specific breed
]

# Add format suffix patterns to allow format-based URLs (e.g., .json, .api)
urlpatterns = format_suffix_patterns(urlpatterns)