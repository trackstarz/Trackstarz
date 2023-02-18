import feedparser

from time import mktime
from datetime import datetime

from django.core.management.base import BaseCommand

from blog.models import Burst

class Command(BaseCommand):
    args = ''
    help = 'Gets N recent blog posts. Better than parsing the list every page load.'

    def handle(self, arg, **options):
        num_blog_posts = int(arg)

        feed = feedparser.parse('http://trackstarz.com/feed/')

        loop_max = num_blog_posts if len(feed['entries']) > num_blog_posts else len(feed['entries'])

        for i in range(0, loop_max):
            if feed['entries'][i]:
                blog_post = RecentBlogPosts()
                blog_post.title = feed['entries'][i].title
                blog_post.bodytext = feed['entries'][i].description
                blog_post.timestamp = datetime.fromtimestamp(mktime(feed['entries'][i].published_parsed))
                blog_post.save()
