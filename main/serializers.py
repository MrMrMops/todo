from rest_framework import serializers
from .models import todo


class TodoSerializer(serializers.ModelSerializer):
    # creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = todo
        fields = '__all__'