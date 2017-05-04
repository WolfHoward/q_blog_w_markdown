from django.contrib.syndication.views import Feed
from blog.models import Entry


class LatestPosts(Feed):
    title= "Q Blog"
    link = "/feed/"
    descripton = "Latest posts of Q"

    def items(self):
        return Entry.objects.published()[:5]
