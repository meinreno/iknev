from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from iknev_process.models import Process, Action, ProcessWay
from iknev_process.serializers import (ProcessSerializer, ActionSerializer,
                                        ProcessWaySerializer)

@api_view(['GET'])
def processes(request):
    if request.method == 'GET':
        processes = Process.objects.all()
        serializer = ProcessSerializer(processes, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def process(request, pk=None):
    if request.method == 'POST':
        serializer = ProcessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        try:
            process = Process.objects.get(id=pk)
        except Process.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = ProcessSerializer(process)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = ProcessSerializer(process, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            process.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def actions(request):
    if request.method == 'GET':
        actions = Action.objects.all()
        serializer = ActionSerializer(actions, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def processes_ways(request):
    if request.method == 'GET':
        actions = ProcessWay.objects.all()
        serializer = ProcessWaySerializer(actions, many=True)
        return Response(serializer.data)