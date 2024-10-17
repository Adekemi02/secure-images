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

app_name = 'library'

urlpatterns = [

    # ex: /library/
    re_path(r'^$', views.index, name='index'),

    # ex: /library/books/<ISBN>
    re_path(r'^books/(?P<ISBN>[0-9-A-Za-z]+)/$', views.book_detail, name='books'),
]
