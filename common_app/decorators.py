from functools import wraps

from django.core.exceptions import PermissionDenied

from common_app.models import Article


def user_is_article_author(view):
    @wraps(view)
    def wrap(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if article.user == request.user.profile:
            return view(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap
