from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.urls import reverse

class BlogSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.5
    def items(self):
        return Post.objects.all()
    def lastmod(self, obj):
        return obj.published_date
    # def location(self, item):
    #     return reverse('post_detail', args=[item.id])