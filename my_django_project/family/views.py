from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Suggestion, Like
from .forms import PostForm, CommentForm, SuggestionForm

@login_required
def wall(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('wall')
    else:
        form = PostForm()
    
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'family/wall.html', {'posts': posts, 'form': form})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
    return redirect('wall')

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
    return redirect('wall')

@login_required
def suggestions(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.author = request.user
            suggestion.save()
            return redirect('suggestions')
    else:
        form = SuggestionForm()
    
    suggestions_list = Suggestion.objects.all().order_by('-created_at')
    return render(request, 'family/suggestions.html', {'suggestions': suggestions_list, 'form': form})
