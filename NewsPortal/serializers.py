from news.models import Post, Category, Author, User
from rest_framework import serializers


class NewsSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Post
       fields = ['id', 'post_type', 'post_category', 'post_author', 'post_create_date', 'post_header', 'post_text']


class ArticlesSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Post
       fields = ['id', 'post_type', 'post_category', 'post_author', 'post_create_date', 'post_header', 'post_text']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Category
       fields = ['id', 'category_name']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Author
       fields = ['id', 'author_user']

class UserSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = User
       fields = ['id', 'username']