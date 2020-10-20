from django.utils import timezone
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from datetime import date
from serviceapply.models import Service


def mainpage(request):
    return render(request, 'community/mainpage.html')


def post_list(request, service="공군 전산병"):
    services = Service.objects.all()
    posts = Post.objects.filter(service=service).order_by('-published_date')
    work_hardness =0
    work_happyness = 0
    work_env = 0
    night_work_frequency = 0
    self_dev = 0
    for post in posts:
        work_hardness += post.work_hardness
        work_happyness += post.work_happyness
        work_env += post.work_env
        night_work_frequency += post.night_work_frequency
        self_dev += post.self_dev
    if(len(posts) != 0):
        work_env /= len(posts)
        work_happyness /= len(posts)
        work_hardness /= len(posts)
        night_work_frequency /= len(posts)
        self_dev /= len(posts)
        datas = [work_hardness, work_happyness, work_env, night_work_frequency, self_dev]
    return render(request, 'community/post_list.html', {'posts': posts, 'services': services, "datas":datas})


def prepare(request):
    return render(request, 'community/prepare.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = comment_list(post)
    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.published_date = timezone.now()
            form.post = post
            form.author = request.user
            form.save()
            return redirect('post_detail', pk=post.id)
    else:
        form = CommentForm(request.POST)
    return render(request, 'community/post_detail.html',
                  {'post': post, 'comments': comments, 'form': form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            print(form.cleaned_data['work_hardness'])
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.service = form.cleaned_data['service']
            post.work_hardness = form.cleaned_data['work_hardness']
            post.work_happyness = form.cleaned_data['work_happyness']
            post.work_env = form.cleaned_data['work_env']
            post.night_work_frequency = form.cleaned_data['night_work_frequency']
            post.self_dev = form.cleaned_data['self_dev']
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'community/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid() and request.user.is_authenticated:
            print(form.cleaned_data['work_hardness'])
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.service = form.cleaned_data['service']
            post.work_hardness = form.cleaned_data['work_hardness']
            post.work_happyness = form.cleaned_data['work_happyness']
            post.work_env = form.cleaned_data['work_env']
            post.night_work_frequency = form.cleaned_data['night_work_frequency']
            post.self_dev = form.cleaned_data['self_dev']
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'community/post_edit.html', {'form': form})

def post_like(request, pk=1):
    user_input = request.GET.get('value')
    post = get_object_or_404(Post, pk=pk)
    if request.method == "GET":
        post.like = post.like+1
        post.save()
    return HttpResponse(post.like)
    
def comment_list(post):
    comments = Comment.objects.filter(post=post).order_by('-published_date')
    return comments

def test(request):
    user_input = request.GET.get('value')
    #put your code here
    return HttpResponse('what you want to output to web')


def test(request):
    user_input = request.GET.get('value')
    #put your code here
    return render(request, "community/test2.html");
