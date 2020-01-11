from rest_framework import serializers
from .models import Question

class RTQASerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'title', 'description', 'completed')