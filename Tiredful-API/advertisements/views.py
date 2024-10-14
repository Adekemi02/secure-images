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

from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from advertisements.models import Classified
from advertisements.serializers import ClassifiedSerializers


# Index for rendering the advertisements page
def index(request):
    """
    Index for advertisements page
    """
    return render(request, 'advertisements/index.html', context={})


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def advertisements(request):
    """
    List of advertisements posted
    """
    if request.method == 'GET':
        classifieds = Classified.objects.all()
        serializer = ClassifiedSerializers(classifieds, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ClassifiedSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Pass user as a keyword argument
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

