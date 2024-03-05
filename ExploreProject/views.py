"""
ExploreProject Views.
"""
from django.views.generic import (
    TemplateView,
)


class HomeView(TemplateView):
    """Home page "View."""
    template_name = 'home.html'
    # template_name = 'account/login.html'
    # template_name = 'account/register.html'