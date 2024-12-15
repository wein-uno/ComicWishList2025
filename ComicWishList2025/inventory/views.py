# inventory/views.py
from django.shortcuts import render, redirect
from .forms import ComicForm

def add_comic(request):
    if request.method == 'POST':
        form = ComicForm(request.POST, request.FILES)
        if form.is_valid():
            comic = form.save(commit=False)  # Do not save to the database yet
            if 'image' in request.FILES:  # Check if image is in the request
                comic.image = request.FILES['image'].read()  # Read the image as binary data
            comic.save()  # Now save the comic with the image data
            return redirect('comic_list')
    else:
        form = ComicForm()
    
    return render(request, 'inventory/add_comic.html', {'form': form})

def comic_list(request):
    comics = Comic.objects.all()  # Fetch all comics from the database
    return render(request, 'inventory/comic_list.html', {'comics': comics})

from django.http import HttpResponse
from .models import Comic

def view_comic_image(request, comic_id):
    comic = Comic.objects.get(pk=comic_id)
    if comic.image:
        return HttpResponse(comic.image, content_type="image/jpeg")  # You can adjust the content type if needed
    else:
        return HttpResponse("No image available", content_type="text/plain")
