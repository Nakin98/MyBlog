from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.list import ListView
from django.urls import reverse
from .models import Comment, PostModel
from .forms import CommentForm, PostModelForm
from django.http import  HttpResponseRedirect
from django.contrib.auth.models import User


class HomeView(ListView):
    queryset = PostModel.objects.all()
    template_name = 'core/homepage.html'
    context_object_name = "lista_post"
    



def post(request, pk):
    template_name = 'core/post.html'
    post = get_object_or_404(PostModel, pk=pk)
    user = request.user
    comments = post.comments.all().filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = user
            new_comment.save()
            return HttpResponseRedirect(reverse('post_singolo', kwargs={'pk': pk}))
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})



def crea_post(request):
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            post = PostModel.objects.create(
                autore = request.user,
                titolo = form.cleaned_data["titolo"],
                contenuto = form.cleaned_data["contenuto"],
                argomento = form.cleaned_data["argomento"],
            )
            post.save()
            return HttpResponseRedirect('') #post.get_absolute_url()
    else:
        form = PostModelForm()
    context = {"form":form}
    return render(request, "core/crea_post.html", context)




def cerca(request):
    if "q" in request.GET:
        querystring = request.GET.get("q")
        print(querystring)
        if len(querystring) == 0:
            return redirect("/cerca/")
        posts = PostModel.objects.filter(titolo__icontains=querystring)
        context = { "posts": posts }
        return render(request, 'core/cerca.html', context)
    else:
        return render(request, 'core/cerca.html')