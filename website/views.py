from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def patients(request):
    return render(request, 'patients.html', {})

def services(request):
    return render(request, 'services.html', {})

def news(request):
    return render(request, 'news.html', {})

def contact(request):
    if request.method == 'POST':
        if 'appoinment-submit' in request.POST:
            first_name = request.POST.get('first-name', False)
            last_name = request.POST.get('last-name', False)
            visit_date = request.POST.get('visit-date', False)
            appoinment_email = request.POST.get('appoinment-email', False)
            treatment = request.POST.get('treatment', False)
            note = request.POST.get('note', False)
            # send an appointment email
            send_mail(
                f"Appintment for: {first_name} {last_name}", # subject
                f"Appiontment for : {first_name} {last_name}\nEmail: {appoinment_email}\n\nOn: {visit_date}\nTreatment: {treatment}\nNote: {note}", # message
                appoinment_email, # from email
                ['andreanistormar@gmail.com'], # to email
            )
            return render(request, 'contact.html', {
                'message_name': first_name
            })
        
        elif 'message-submit' in request.POST:
            full_name = request.POST.get('full-name', False)
            email = request.POST.get('client-email', False)
            message = request.POST.get('message', False)
            # send message email
            send_mail(
                f"Message from: {full_name}", # subject
                f"Contact email: {email}\n{message}", # message
                email, # from email
                ['andreanistormar@gmail.com'] # to email
            )
            return render(request, 'contact.html', {
                'message': 'Thank you for your message.'
            })
    return render(request, 'contact.html', {})