# -*- coding: utf-8 -*-
#
#   ____  __  ___   ___  ___  ___  _  _  __       __   ___  __
#  (_  _)(  )(  ,) (  _)(   \(  _)( )( )(  )     (  ) (  ,\(  )
#   )(   )(  )  \  ) _) ) ) )) _) )()(  )(__    /__\  ) _/ )(
#  (__) (__)(_)\_)(___)(___/(_)   \__/ (____)  (_)(_)(_)  (__)
#
#
# Copyright (C) 2017-2018 Payatu Software Labs

from django.urls import re_path, include
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Define the base URL for the API version
API_VERSION = r'^api/v1/'

# First we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Specify the fields you want to include

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'  # Specify the fields you want to include

urlpatterns = [
    # URL for user login
    re_path(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # URL for including intro app.
    re_path(r'', include('intro.urls', namespace="intro")),

    # URLs for including library app
    re_path(API_VERSION, include('library.urls', namespace="library-api")),
    re_path(r'^library/', include('library.urls', namespace="library")),

    # URLs for including exams app
    re_path(API_VERSION, include('exams.urls', namespace="exams-api")),
    re_path(r'^exams/', include('exams.urls', namespace="exams")),

    # URLs for including blog app
    re_path(API_VERSION, include('blog.urls', namespace="blog-api")),
    re_path(r'^blog/', include('blog.urls', namespace="blog")),

    # URLs for including trains app
    re_path(API_VERSION, include('trains.urls', namespace="trains-api")),
    re_path(r'^trains/', include('trains.urls', namespace="trains")),

    # URLs for including health app
    re_path(API_VERSION, include('health.urls', namespace="health-api")),
    re_path(r'^health/', include('health.urls', namespace="health")),

    # URLs for including advertisements app
    re_path(API_VERSION, include('advertisements.urls', namespace="advertisements-api")),
    re_path(r'^advertisements/', include('advertisements.urls', namespace="advertisements")),
]
