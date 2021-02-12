"""Routing/URLs configuration.

`urlpatterns` provides a list of routes from an URL path to a view.

Paths must start without leading slash and end with a trailing slash.
    - Good: `""`, `"home/"`, `"path/to/page-name/"`.
    - Bad: `"/"`, `"home"`, `"/path/to/page-name/"`.

Best Practices:
    - Paths: Use only `[a-z\-/]` (i.e. all lowercase and only "-" and "/").
    - Route names: Use only `[a-z_]` (i.e. all lowercase and only "_", no "-").

Examples:
    - Function views:
        1. Imports: `from my_app import views`
        2. URL patterns: `path("", views.home, name="home_page")`
    - Class-based views:
        1. Imports: `from other_app.views import FooBar`
        2. URL patterns: `path("foo-bar/", FooBar.as_view(), name="foo_bar")`
    - Including another URLconf:
        1. Imports: `from django.urls import include`
        2. URL patterns: `path("blog/", include("blog.urls"))`

[URLs documentation](https://docs.djangoproject.com/en/3.1/topics/http/urls/)
"""
from django.apps import apps
from django.conf import settings
from django.urls import include, path
# // from django.utils.translation import gettext_lazy as _
# // from django.views.generic.base import TemplateView


urlpatterns = []


# SITEMAP ==========================================================================================
# Doc: https://docs.djangoproject.com/en/3.1/ref/contrib/sitemaps/

# // from django.contrib.sitemaps import views as sitemaps_views
# // from django.views.decorators.cache import cache_page
# //
# // from %PROJECT_SNAKE%.%APP_NAME%.sitemap import %MODEL%Sitemap
# //
# //
# // SITEMAPS_BASE_URL = getattr(settings, "SITEMAPS_BASE_URL", "")
# // SITEMAPS = {
# //     "%SITEMAP_NAME%": %MODEL%Sitemap,
# // }
# //
# // urlpatterns += [
# //     path(
# //         f"{SITEMAPS_BASE_URL}sitemap.xml",
# //         cache_page(settings.SITEMAPS_CACHE_TIMEOUT)(sitemaps_views.index),
# //         {"sitemaps": SITEMAPS, "sitemap_url_name": "sitemaps"},
# //     ),
# //     path(
# //         f"{SITEMAPS_BASE_URL}sitemap-<section>.xml",
# //         cache_page(settings.SITEMAPS_CACHE_TIMEOUT)(sitemaps_views.sitemap),
# //         {"sitemaps": SITEMAPS},
# //         name="sitemaps",
# //     ),
# // ]


# ADMIN ============================================================================================

from django.contrib import admin


# Best Practices: Always provide a fake login on "admin/".
# pip:django-admin-honeypot
urlpatterns += [path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot"))]

# If `ADMIN_BASE_URL` is not defined, it means that it must not be activated.
ADMIN_BASE_URL = getattr(settings, "ADMIN_BASE_URL", None)
if ADMIN_BASE_URL:
    urlpatterns += [path(ADMIN_BASE_URL, admin.site.urls)]
else:
    # If no admin, provide anyway a prefix for admin tools.
    ADMIN_BASE_URL = "admin-"

# pip:django-rosetta
if apps.is_installed("rosetta"):
    urlpatterns += [path(f"{ADMIN_BASE_URL}rosetta/", include("rosetta.urls"))]


# APPLICATION ======================================================================================

from django.views.i18n import set_language  # // JavaScriptCatalog


# ROUTES WITHOUT LANGUAGE PREFIX -------------------------------------------------------------------

# Non-translated URLs without language prefix.
# // urlpatterns += [
# //     path("", TemplateView.as_view(template_name="home.html"), name="home"),
# //     path("%NAME%/", include("%PROJECT_SNAKE%.%MODULE%.urls")),
# //     path("setlang/", set_language, name="set_language"),
# // ]

# Translated URLs without language prefix.
# // urlpatterns += [
# //     path(_("%NAME%/"), include("%PROJECT_SNAKE%.%MODULE%.urls")),
# // ]


# ROUTES WITH LANGUAGE PREFIX ----------------------------------------------------------------------
# // from django.conf.urls.i18n import i18n_patterns
# //
# // Non-translated URLs with language prefix.
# // urlpatterns += i18n_patterns(
# //     path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
# //     path("foo/", TemplateView.as_view(template_name="pages/foo.html"), name="foo"),
# //     path("jsi18n/", JavaScriptCatalog.as_view(), name="js-catalog"),
# // )
# //
# // Translated URLs with language prefix.
# // urlpatterns += i18n_patterns(
# //     path("blog/", include("blog.urls")),
# // )


# APP MODE: LOCAL ==================================================================================

if settings.APP_MODE == "local":
    # Serving static files.
    from django.conf.urls.static import static
    if settings.STATIC_ROOT:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# DEBUG ============================================================================================

if settings.DEBUG:
    # Documentation from the docstrings of models, views, template tags,
    #   and template filters for any installed app.
    # Doc: https://docs.djangoproject.com/en/3.1/ref/contrib/admin/admindocs/
    if apps.is_installed("django.contrib.admindocs"):
        urlpatterns += [path(f"{ADMIN_BASE_URL}doc/", include("django.contrib.admindocs.urls"))]

    # pip:django-debug-toolbar
    if apps.is_installed("debug_toolbar"):
        import debug_toolbar
        urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]

    # Allow to test error pages.
    from django.views import defaults as default_views
    urlpatterns += [
        path("__debug__/400/", default_views.bad_request,
             kwargs={"exception": Exception("Bad Request")}),
        path("__debug__/403/", default_views.permission_denied,
             kwargs={"exception": Exception("Forbidden")}),
        path("__debug__/404/", default_views.page_not_found,
             kwargs={"exception": Exception("Not Found")}),
        path("__debug__/500/", default_views.server_error),
    ]
