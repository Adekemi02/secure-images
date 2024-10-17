# -*- coding: utf-8 -*-
#
#   ____  __  ___   ___  ___  ___  _  _  __       __   ___  __
#  (_  _)(  )(  ,) (  _)(   \(  _)( )( )(  )     (  ) (  ,\(  )
#   )(   )(  )  \  ) _) ) ) )) _) )()(  )(__    /__\  ) _/ )(
#  (__) (__)(_)\_)(___)(___/(_)   \__/ (____)  (_)(_)(_)  (__)
#
#
# Copyright (C) 2017-2018 Payatu Software Labs
# This file is part of Tiredful API application

from django.urls import re_path

from . import views

app_name = 'intro'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^about$', views.about, name='about'),
    re_path(r'^scenario$', views.scenario, name='scenario'),
    re_path(r'^handle-user-token/$', views.handle_token, name='handle-user-token'),
    re_path(r'^csrf/$', views.csrf, name='csrf')
]
