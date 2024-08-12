from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Post, Category, Profile
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q



# Signup/SignIn

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        print(username)
        if(password==password2):
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup') 
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signin')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
    else:
        
        return render(request, 'signup.html')
    
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password) 
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('signin')
    else:
        username = "admin"
        password = 123
        return render(request, 'signin.html', {'username':username, 'password':password})
    
@login_required(login_url='signin')
def logout_view(request):
    auth.logout(request)
    return redirect('signin') 

# ----------------------------------
@login_required(login_url='signin')
def BlogListView(request):
    search_query = request.GET.get('search')
    if search_query:
        posts = Post.objects.filter(
            Q(author__icontains=search_query) | 
            Q(title__icontains=search_query) | 
            Q(cat__title__icontains=search_query)
        )
    else:
        posts = Post.objects.all()[:11]
        
    cats = Category.objects.all()
    data = {
        'posts': posts,
        'cats': cats,
    }
    return render(request, 'home.html', data)

@login_required(login_url='signin')
def post(request, url):
    posturl = Post.objects.get(url=url)
    return render(request,'post.html', {'post':posturl})

@login_required(login_url='signin')
def category(request, url):
    search_query = request.GET.get('search')
    if search_query:
        posts = Post.objects.filter(
            Q(author__icontains=search_query) | 
            Q(title__icontains=search_query) 
        )
    else:
        posts = Post.objects.all()
        
    caturl = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=caturl)
    return render(request,'category.html', {'posts':posts, 'caturl':caturl})

@login_required(login_url='signin')
def about(request):
    return  render(request,'about.html')

@login_required(login_url='signin')
def createe(request):
    categories = Category.objects.order_by('title')
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        category_name = request.POST['category']
        image = request.FILES['image']
        url = title
        category = Category.objects.get(title=category_name)
        post = Post.objects.create(title=title, content=content,url=url,  cat=category, image=image, author=author)
        post.save()
        return redirect('/')
    else:
        return render(request, 'create.html', {'categories': categories}) # Redirect to the same page if the data is invalid
    
@login_required(login_url='signin')

def delete_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    url = post.cat.url
    if request.method == 'POST':
        post.delete()
        return redirect('/blogCategories/'+url)  # Replace 'post_list' with the URL name of the view that lists all posts
    return render(request, 'confirm_delete.html', {'post': post})
