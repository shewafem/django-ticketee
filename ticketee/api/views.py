from rest_framework.response import Response
from rest_framework.decorators import api_view
from events.models import Event
from .serializers import EventSerializer



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/event-list/',
        'Detail View': '/event-detail/<int:pk>/',
        'Create': '/event-create/',
        'Update': '/event-update/<int:pk>/',
        'Delete': '/event-delete/<int:pk>/',
    }
    
    return Response(api_urls)


@api_view(['GET'])
def eventList(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def eventDetail(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def eventCreate(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def eventUpdate(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(instance=event, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)



#@api_view(['GET'])
#def apiOverview(request):
#    api_urls = {
        
#    }