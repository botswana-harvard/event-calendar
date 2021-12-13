from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin

from calendarapp.models import Event


class DashboardView(NavbarViewMixin, EdcBaseViewMixin, View):
    # login_url = "accounts:signin"
    template_name = "calendarapp/dashboard.html"
    navbar_selected_item = 'dashboard'
    navbar_name = 'eventcalendar'

    def get(self, request, *args, **kwargs):
        events = Event.objects.get_all_events(user=request.user)
        running_events = Event.objects.get_running_events(user=request.user)
        latest_events = Event.objects.filter(user=request.user).order_by("-id")[:10]
        context = {
            "total_event": events.count(),
            "running_events": running_events,
            "latest_events": latest_events,
        }
        context.update(self.get_context_data())
        return render(request, self.template_name, context)
