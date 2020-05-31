import os
import io

os.environ['DJANGO_SETTINGS_MODULE'] = 'analytics.settings'

from datetime import datetime
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


comment = Comment(email='leila@example.com', content='foo bar')


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance


serializer = CommentSerializer(comment)
print(serializer.data)
print(type(serializer.data))


json = JSONRenderer().render(serializer.data)
print(json)
print(type(json))


stream = io.BytesIO(json)
data = JSONParser().parse(stream)
print(data)
serializer = CommentSerializer(data=data)
print(serializer.is_valid())