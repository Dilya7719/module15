from django.http import HttpResponse
from news.models import Post
import json


def get_new(_, pk):
    new = Post.objects.get(pk=pk)
    data = {"header": new.post_header, "text": new.post_text}
    print(data)
    return HttpResponse(content=data, status=200)

def get_news(_):
    news = Post.objects.filter(post_type='NW')
    return HttpResponse(content=news, status=200)

def create_new(request):
    body = json.loads(request.body.decode('utf-8'))
    new = Post.objects.create(
        post_type='NW',
        post_header=body['header'],
        post_text=body['text'],
        # post_author=???,
        # post_category=???,
    )
    return HttpResponse(content=new, status=201)

def edit_new(request, pk):
    body = json.loads(request.body.decode('utf-8'))
    new = Post.objects.get(pk=pk)
    for attr, value in body.items():
        setattr(new, attr, value)
    new.save()
    data = {"header": new.post_header, "text": new.post_text}
    print(data)
    return HttpResponse(content=data, status=200)

def delete_new(_, pk):
    Post.objects.get(pk=pk).delete()
    return HttpResponse(status=204)

