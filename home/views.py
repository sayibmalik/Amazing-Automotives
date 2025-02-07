from django.shortcuts import render,redirect # type: ignore
from django.core.mail import send_mail # type: ignore

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def team(request):
    return render(request, 'team.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    if request.method == "GET":
       return render(request, 'contact.html')

    if request.method == "POST":
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        send_mail(
            subject="New Contact Form Submission",
            message=f"Name: {first_name} {last_name}\nEmail: {email} \nMessage: {message}",
            from_email="waniarslan250@gmail.com",
            recipient_list=["waniarslan250@gmail.com"],
            fail_silently=False,
        )
        return redirect("/contact")

