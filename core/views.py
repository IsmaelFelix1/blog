from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, FormView, DetailView, ListView
from .models import Post
from .forms import ContatoForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#Pagina Index com GetAll
class IndexView(TemplateView):
    template_name = 'index.html'
    paginate_by = 5

    def get_context_data(self,**kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        post = Post.objects.order_by('-id').all()
        paginator = Paginator(post, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context['post'] = posts
        return context


class SearchResultsView(ListView):
    model = Post
    template_name = 'search/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query))
        return object_list

#Obtendo o get id do objeto
class PostDetailView(DetailView):
    model = Post
    template_name = 'detailpost/detail.html'

    def get_object(self, queryset=None):

        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)


# Formulario na pagina de contato
class ContatoView(FormView):
    template_name = 'contato/contato.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(ContatoView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        form.send_mail()
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(ContatoView, self).form_invalid(form, *args, **kwargs)


class SobreView(TemplateView):
    template_name = 'sobre/sobre.html'