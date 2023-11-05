from django.utils.translation import gettext as _  # импортируем функцию для перевода


# Create your views here.

class Index(View):
    def get(self, request):
        string = _('Hello world')

        return HttpResponse(string)