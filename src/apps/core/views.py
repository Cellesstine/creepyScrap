from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .utils import (
	patterns,
	getPassKey,
	)

from .serializers import (
	NetworkSerializer,
	)

def netInterface(request):
	context = {
		"detail": "creepyscrap.onrender.com only scrap default fiberHome <accessPoint:passKey>"
		}		
	return render(request, "interface.html", context)

@api_view(["POST"])
def networkManager(request):
	serializer = NetworkSerializer(data=request.data)

	if serializer.is_valid():
		accessPoint = serializer.validated_data.get("accessPoint")

		passKey = getPassKey(accessPoint, patterns)

		return Response({"fiberHome <default passKey>": passKey})

	return Response(serializer.errors)