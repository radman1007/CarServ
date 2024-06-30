from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from .models import Contact,Service,Comment,News,Team
from .forms import ContactForm,ServiceForm,CommentForm,NewsForm
def index(request):
    forms = Contact.objects.filter(accept=True)
    forms1 = Team.objects.all()
    context = {
        'forms' : forms,
        'forms1' : forms1,
    }
    return render(request,'index.html',context)

def booking(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking')
    form = ServiceForm()
    context = {
        'form' : form
    }
    return render(request,'booking.html',context)

def about(request):
    forms = Team.objects.filter()
    context = {
        'forms' : forms,
    }
    return render(request,'about.html',context)

def service(request):
    forms = Contact.objects.filter(accept = True)
    context = {
        'forms' : forms,
    }
    return render(request,'service.html',context)

def testimonial(request):
    forms = Contact.objects.filter(accept = True)
    context = {
        'forms' : forms,
    }
    return render(request,'testimonial.html',context)

def team(request):
    forms = Team.objects.filter()
    context = {
        'forms' : forms,
    }
    return render(request,'team.html',context)

def login(request):
    return render(request,'login.html')

def list(request):
    posts = Service.objects.filter()
    context = {
        'posts' : posts,
    }
    return render(request,'list.html',context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    form = ContactForm()
    context = {
        'form' : form,
    }
    return render(request,'contact.html',context)

def post_detail(request,post_id):
    post = get_object_or_404(Service,pk=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            Comment.objects.create(
                name = name,
                email = email,
                message = message,
                post = post,
            )
            return redirect('post_detail',post_id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-created_date')
    form = CommentForm()
    context = {
        'post' : post,'comments' : comments, 'form':form
    }
    return render(request,'post_detail.html',context)


def update(request,post_id):
    if not request.user.is_authenticated:
        return redirect('login')
    post = get_object_or_404(Service,pk=post_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('list')
    form = ServiceForm(instance=post)
    context = {
        'post' : post,
        'form' : form
    }
    return render(request , 'update.html' , context)

def delete(request,post_id):
    if not request.user.is_authenticated:
        return redirect('login')
    post = get_object_or_404(Service,pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('list')
    context = {
        'post' : post
    }
    return render(request , 'delete.html' , context)