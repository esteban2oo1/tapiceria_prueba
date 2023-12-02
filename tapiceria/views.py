from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

def load_image(request, image_name):
    # Assuming the images are stored in a directory named "imagenes" within your static files
    image_path = os.path.join(settings.MEDIA_ROOT, 'producto', image_name)
    print(image_path)
    try:
        with open(image_path, 'rb') as image_file:
            # Determine the image's content type
            content_type = 'image/jpeg'  # You may need to adjust this based on your image types
            response = HttpResponse(image_file.read(), content_type=content_type)
            return response
    except FileNotFoundError:
        # Handle the case when the image file is not found
        return HttpResponse('Image not found', status=404)
