from django.shortcuts import render
from rest_framework import viewsets
from .models import State
from .serializers import StateSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import State

# Create your views here.
class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    @action(detail=False, methods=['POST'])
    def load_states(self, request, *args, **kwargs):
        json = request.data.get('estados')
        for data in json:
            State.objects.create(name=data['name'], abbreviation=data['abbreviation'])
        return Response('Estados cargados correctamente')