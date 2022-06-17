from rest_framework import serializers
from .models import Article



class ArticlesSerializers(serializers.Serializer):

    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateField()


    def create(self,validated_data):
       return  Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.author = validated_data.get('author',instance.author)
        instance.date = validated_data.get('date',instance.date)
        instance.save()
        return instance

       
        


