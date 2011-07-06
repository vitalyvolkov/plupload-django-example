from django.contrib import admin
from models import Article, Photo
from forms import PhotoForm
from django.conf import settings
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def upload(request, id):
    if not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden(
            'You should be authenticated as admin or staff to upload files')
    article = get_object_or_404(Article, id=id)
    
    form = PhotoForm(request.POST, request.FILES)
    if form.is_valid():
        p = form.save(commit = False)
        p.article = article
        p.save()
    return HttpResponse('')


class PhotoAdmin(admin.ModelAdmin):
    
    list_display = ((lambda x: x.article.title), 'file', )
    
    
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ('title', )
    change_form_template = 'article_change_form.html'
    
    class Media:
        js = (
              settings.MEDIA_URL+'plupload/plupload.full.js',
              '%splupload/jquery.plupload.queue/jquery.plupload.queue.js' % (
                    settings.MEDIA_URL),
        )
        css = {"all": (
            '%splupload/jquery.plupload.queue/css/jquery.plupload.queue.css' % (
                settings.MEDIA_URL),)
        }
    
    
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Article, ArticleAdmin)