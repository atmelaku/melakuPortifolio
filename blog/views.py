from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import  (

                ListView,
                DetailView,
                CreateView,
                UpdateView,
                DeleteView
            )
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import (
                LoginRequiredMixin,
                UserPassesTestMixin
                )
from .forms import UploadImages, EditImageForm
from .models import Images

def home(request):

    context = {
    "posts": Post.objects.all()
    }

    return render(request, "blog/home.html", context)
# about
def about(request):
    return render(request, "blog/about.html")
# resume
def resume(request):
    return render(request, "blog/resume.html")

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_post.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # this is for ckecking exact user is updating its own post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


from django.contrib import messages

def gallery(request):
    if request.method == "POST":
        img_form = UploadImages(request.POST, request.FILES)
        if img_form.is_valid():
            img_form.save()
            messages.success(request, "Image uploaded successfully.")
            return redirect("blog-gallery")
    else:
        img_form = UploadImages()

    images = Images.objects.all()  # Assuming ImageModel is your model for storing images

    context = {
        "image_form": img_form,
        "images": images,
    }

    return render(request, "blog/gallery.html", context)

def delete_image(request, image_id):
    image = get_object_or_404(Images, pk=image_id)
    if request.method == "POST":
        image.delete()
        messages.success(request, "Image deleted successfully.")
        return redirect("blog-gallery")
    context = {
        "image": image
    }

    return render(request, "blog/delete_image_confirm.html", context)

def edit_image(request, image_id):
    image = get_object_or_404(Images, pk=image_id)
    if request.method == "POST":
        form = EditImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, "Image and description updated successfully.")
            return redirect("blog-gallery")
    else:
        form = EditImageForm(instance=image)
    context = {
        "form": form,
        "image": image
    }

    return render(request, "blog/edit_image.html", context)
