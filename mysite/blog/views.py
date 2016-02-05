from django.views import generic
from django.utils import timezone

from .models import Post


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Post.objects.filter(date__lte=timezone.now())
