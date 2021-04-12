from django.shortcuts import render, redirect
from .forms import *


def post_book_view(request):
    user = PublisherProfileModel.objects.get(user=request.user)
    task = "Post New"
    form = PostBookForm()
    if request.method == 'POST':
        form = PostBookForm(request.POST, request.FILES)
        if form.is_valid():
            new_ad = form.save(commit=False)
            new_ad.publisher = user
            form.save()
            return redirect('home')
        else:
            context = {
                'task': task,
                'form': form
            }
            return render(request, 'book_control/post-update-book.html', context)

    context = {
        'task': task,
        'form': form
    }
    return render(request, "publisher/post-update-book.html", context)
