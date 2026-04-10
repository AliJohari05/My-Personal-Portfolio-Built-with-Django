"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from blog.sitemaps import BlogSitemap
from portfolio import views
from portfolio import views as portfolio_views
from blog import views as blog_views
from ai_lab import views as ai_lab_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from portfolio.sitemaps import StaticViewSitemap
sitemaps = {'static': StaticViewSitemap,
            'blog': BlogSitemap,}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('',views.home_page,name='home'),
    path('portfolio/', portfolio_views.portfolio_page, name='portfolio'),
    path('category/<slug:category_slug>/', views.portfolio_page, name='portfolio_category'),
    path('portfolio/<int:project_id>',portfolio_views.project_detail, name='project_detail'),
    path('blog/', blog_views.blog_page, name='blog'),
    path('blog/<int:post_id>/', blog_views.post_detail, name='post_detail'),
    path('category/<str:category_name>/', blog_views.category_posts, name='category_posts'),
    path('ai-lab/', ai_lab_views.ai_lab_page, name='ai_lab'),
    path('contact/', portfolio_views.contact_page, name='contact'),
    path('ai-lab/<slug:slug>/', ai_lab_views.ai_lab_detail, name='ai_lab_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)