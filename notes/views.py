from django.shortcuts import render
from django.http import Http404  # 404 error
from django.http import HttpResponseRedirect  # redirect

# class based views
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Notes

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404('Note does not exist')
#     return render(request, 'notes/notes_details.html', {'note': note})

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = "/smart/notes"
    template_name = "notes/notes_delete.html"


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = "/smart/notes"
    form_class = NotesForm


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    # fields = ['title', 'text']
    success_url = "/smart/notes"
    form_class = NotesForm
    login_url = "/login"

    def form_valid(self, form):
        #  create an object from the form but don't save it to the database
        self.object = form.save(commit=False)
        #  set the user of the object to the current user
        self.object.user = self.request.user
        self.object.save()  #  save the object to the database
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/login"  #  redirects to admin login page if user is not logged in

    def get_queryset(self):
        return self.request.user.notes.all()

# no need to handle 404 error, it is handled by the class based view


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_details.html"
