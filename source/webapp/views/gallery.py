from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from webapp.models import Gallery

from webapp.forms import GalleryForm


class GalleryView(ListView):
    template_name = "gallery.html"
    model = Gallery
    context_object_name = "posts_view"


class GalleryCreateView(LoginRequiredMixin, CreateView):
    template_name = "gallery_create.html"
    model = Gallery
    form_class = GalleryForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            signature = form.cleaned_data.get('signature')
            photo = form.cleaned_data.get('photo')
            user = request.user
            Gallery.objects.create(signature=signature, photo=photo, author=user)
        return redirect('index')


class GalleryUpdateView(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    model = Gallery
    template_name = "gallery_update.html"
    form_class = GalleryForm
    permission_required = 'webapp.change_gallery'
    context_object_name = 'gallery'

    def get_success_url(self):
        return reverse_lazy('detail_view', kwargs={'pk': self.object.pk})


class GalleryDetailView(TemplateView):
    template_name = "detail_gallery.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = get_object_or_404(Gallery, pk=kwargs['pk'])
        return context


class GalleryDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'delete_confirm.html'
    model = Gallery
    context_object_name = 'task'
    permission_required = 'webapp.delete_gallery'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        return self.delete(request)



