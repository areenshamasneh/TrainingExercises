from rest_framework import serializers # type: ignore
from polls.models import Poll, Choice

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['id', 'question', 'pub_date']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'poll', 'choice_text', 'votes']
