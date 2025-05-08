#I have created this file --Shubham
from django.http import HttpResponse
from django.shortcuts import render



def about(request):
    return HttpResponse("About Shubham Chakravarty")

def removepun(request):
    return HttpResponse("Remove Punc")

def home(request):
    products = [
        {'title': 'Wireless Headphones', 'description': 'Noise cancelling, long battery life.', 'image': 'box2_image.jpg'},
        {'title': 'Smartwatch', 'description': 'Track fitness and stay connected.', 'image': 'box1_image.jpg'},
        {'title': 'Gaming Mouse', 'description': 'High precision and customizable.', 'image': 'box3_image.jpg'},
        {'title': 'Bluetooth Speaker', 'description': 'Powerful sound on the go.', 'image': 'box4_image.jpg'},
        {'title': 'LED Monitor', 'description': 'Full HD display, crisp visuals.', 'image': 'box5_image.jpg'},
        {'title': 'DSLR Camera', 'description': 'Capture memories in high definition.', 'image': 'box6_image.jpg'},
        {'title': 'Fitness Band', 'description': 'Track your steps and sleep.', 'image': 'box7_image.jpg'},
        {'title': 'E-Book Reader', 'description': 'Read books anytime, anywhere.', 'image': 'box8_image.jpg'},
    ]
    return render(request, 'index.html', {'products': products})
