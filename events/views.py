from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from .models import Event, EventNumbers, CommentEvent
from .forms import EventForm, EventCommentForm
from datetime import date


class EventList(ListView):
    """
    Create a list of events view
    """
    model = Event
    template_name = "events/events.html"
    context_object_name = "events"
    paginate_by = 6
    
    def get_queryset(self): 
        events = Event.objects.filter(e_time__gt=date.today()).order_by("-e_time")
        return events


class CreateEventView(LoginRequiredMixin, CreateView):
    """
    Create an event view
    """
    form_class = EventForm
    model = Event
    template_name = "events/create_event.html"
    success_url = "/events/events"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateEventView, self).form_valid(form)


class EventDetailView(LoginRequiredMixin, FormMixin, DetailView):
    """
    Event details view
    """
    model = Event
    template_name = "events/view_event.html"
    context_object_name = 'event'

    def post(self, request, pk):
        event = Event.objects.filter(id=pk)[:1].get()
        user = EventNumbers.objects.filter(user=self.request.user, event=event)
    
        if user:
            user.delete()
        else:
            EventNumbers.objects.create(
                user=self.request.user,
                event=event,
            )

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    def get_context_data(self, **kwargs):
        data = self.get_object()

        going_event = EventNumbers.objects.filter(user=self.request.user, event=data)
        comments = CommentEvent.objects.filter(event=data.pk)

        context = {
            "event": data,
            "number": EventNumbers.objects.filter(event=self.kwargs['pk']).count,
            "going_event": going_event,
            'form': EventCommentForm(),
            'comments': comments
        }
        return context


class CommentEventView(LoginRequiredMixin, CreateView):
    model = CommentEvent
    form_class = EventCommentForm

    def form_valid(self, form):
        # if form is valid return to post
        pk = self.kwargs['pk']
        self.success_url = f'/events/view/{pk}/'
        form.instance.event = Event.objects.get(id=self.kwargs['pk'])
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditEventView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to editing an event form for the event owner
    """
    form_class = EventForm
    template_name = "events/edit_event.html"
    model = Event

    def form_valid(self, form):
        self.success_url = "/events/events"
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteEventView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view to delete a post
    """
    model = Event
    success_url = "/events/events"

    def test_func(self):
        return self.request.user == self.get_object().user
