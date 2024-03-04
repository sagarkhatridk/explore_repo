"""
ExploreProject Views.
"""
from django.views.generic import (
    TemplateView,
)


class HomeView(TemplateView):
    """Home page "View."""
    template_name = 'accounts/login.html'