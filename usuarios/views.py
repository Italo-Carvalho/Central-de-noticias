from django.shortcuts import render
from .forms import CustomUsuarioCreateForm
from django.views.generic.edit import FormView


class UsercreateFormView(FormView):
    form_class = CustomUsuarioCreateForm
    template_name = 'cadastro.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(UsercreateFormView, self).form_valid(form)
