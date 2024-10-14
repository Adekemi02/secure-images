# -*- coding: utf-8 -*-
#
#   ____  __  ___   ___  ___  ___  _  _  __       __   ___  __
#  (_  _)(  )(  ,) (  _)(   \(  _)( )( )(  )     (  ) (  ,\(  )
#   )(   )(  )  \  ) _) ) ) )) _) )()(  )(__    /__\  ) _/ )(
#  (__) (__)(_)\_)(___)(___/(_)   \__/ (____)  (_)(_)(_)  (__)
#
#
# Copyright (C) 2017-2018 Payatu Software Labs

from django.conf.urls import url, include
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
    url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # URL for including intro app.
    url(r'', include('intro.urls', namespace="intro")),

    # URLs for including library app
    url(API_VERSION, include('library.urls', namespace="library-api")),
    url(r'^library/', include('library.urls', namespace="library")),

    # URLs for including exams app
    url(API_VERSION, include('exams.urls', namespace="exams-api")),
    url(r'^exams/', include('exams.urls', namespace="exams")),

    # URLs for including blog app
    url(API_VERSION, include('blog.urls', namespace="blog-api")),
    url(r'^blog/', include('blog.urls', namespace="blog")),

    # URLs for including trains app
    url(API_VERSION, include('trains.urls', namespace="trains-api")),
    url(r'^trains/', include('trains.urls', namespace="trains")),

    # URLs for including health app
    url(API_VERSION, include('health.urls', namespace="health-api")),
    url(r'^health/', include('health.urls', namespace="health")),

    # URLs for including advertisements app
    url(API_VERSION, include('advertisements.urls', namespace="advertisements-api")),
    url(r'^advertisements/', include('advertisements.urls', namespace="advertisements")),
]
