from rest_framework import serializers
from .models import *
from books.serializers import BooksSerializer


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'


class LibraryActivitySerializer(serializers.ModelSerializer):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['library'] = serializers.SerializerMethodField(read_only=True)
    #     self.fields['book'] = serializers.SerializerMethodField(read_only=True)
    #
    # def get_library(self, instance):
    #     return LibrarySerializer(instance=instance).data
    #
    # def get_book(self, instance):
    #     return BooksSerializer(instance=instance).data

    class Meta:
        model = LibraryActivities
        fields = '__all__'