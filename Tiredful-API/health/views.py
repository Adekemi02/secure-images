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
from django.db import connection
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from health.models import Tracker
from health.serializers import TrackerSerializers


# Index method for Blog article listing
def index(request):
    """
    Index page for health application
    """
    tracker_details = Tracker.objects.all()
    return render(request, 'health/index.html', {'tracker_details': tracker_details})

# Helper function to serialize activities
def serialize_activities(activities):
    return [TrackerSerializers(activity).data for activity in activities]

# get user activities
@api_view(['POST'])
def get_activity(request):
    """
    Details of user activity monthwise
    """
    month_requested = request.data.get('month')

    # Check for missing month in request data
    if not month_requested:
        return Response({"error": "Month is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Use Django ORM instead of raw SQL
        activity_detail = Tracker.objects.filter(month=month_requested)

        # Check if any activities were found
        if not activity_detail.exists():
            return Response({"error": "No activities found for the given month."}, status=status.HTTP_404_NOT_FOUND)

        # Serialize and return the data
        final_serialized_data = serialize_activities(activity_detail)
        return Response(final_serialized_data)

    except Exception as e:
        # Log exception (if you have a logging system)
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    