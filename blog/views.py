from django.shortcuts import render, redirect
from .models import Post, Comment

def index(request):
    return render(request,'index.html' )

def post_list(request):
    posts = Post.objects.order_by('-id') # 새로운 것이 위로 오게하기
    context = {
        "posts":posts
    }
    return render(request, "post_list.html", context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        comment_content = request.POST['comment']
        Comment.objects.create(
            post=post,
            content=comment_content,
        )

    context = {
        "post":post,
    }
    return render(request, "post_detail.html", context)



def post_add(request):
    if request.method == "POST":
        print(request.FILES)
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES['thumbnail']
        post = Post.objects.create(
            title = title,
            content = content,
            thumbnail = thumbnail,
        )
        return redirect(f"/posts/{post.id}/") # posts/ 로 하면 뒤에 붙고, /posts/ 로 하면 8000/뒤에 붙는다
    
    else:
        print("method GET")
    return render(request, "post_add.html")

