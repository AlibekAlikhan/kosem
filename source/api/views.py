import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from webapp.models import Gallery


@csrf_exempt
def favorites_api(request, *args, **kwargs):
    if request.method == "POST":
        article = json.loads(request.body)
        user = request.user
        print(article.get('A'))
        post = Gallery.objects.get(pk=article.get('A'))
        if user not in post.favorites.all():
            post.favorites.add(user)
        else:
            post.favorites.remove(user)
        return JsonResponse({"": ""})