from rest_framework import viewsets # type: ignore
from rest_framework.response import Response # type: ignore
from polls.models import Poll, Choice
from polls.serializers import PollSerializer, ChoiceSerializer

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        poll_id = self.kwargs.get('poll_pk')
        return Choice.objects.filter(poll=poll_id)
