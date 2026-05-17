from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.

from .models import Contact, Projet, Certifications, Experience, Formation, Cv


def index(request):

    projets = Projet.objects.all().order_by('-date_created')  # Affiche les projets les plus récents en premier
    certifications = Certifications.objects.all()
    experiences = Experience.objects.all().order_by('-date_debut')  # Affiche les expériences les plus récentes en premier
    formation = Formation.objects.all().order_by('-date_debut')
    cv = Cv.objects.last()  # Récupère le dernier CV ajouté

    context = {
        'projets': projets,
        'certifications': certifications,
        'experiences': experiences,
        'formation': formation,
        'cv': cv,
    }

    return render(request, "app/index.html", context)


def project_detail(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    context = {
        'projet': projet,
    }
    return render(request, "app/project_detail.html", context)



@require_http_methods(['POST'])
def ajax_contact_create(request):
    """Reçoit les données du formulaire contact via AJAX."""
    nom = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    message = request.POST.get('message', '').strip()

    if not nom or not email or not message:
        return JsonResponse({'error': 'Tous les champs sont requis.'}, status=400)

    contact = Contact.objects.create(nom=nom, email=email, message=message)

    return JsonResponse({'success': True, 'message': 'Message envoyé avec succès !', 'contact_id': contact.id}, status=201)


@require_http_methods(['GET'])
def ajax_contact_list(request):
    """Retourne tous les contacts enregistrés en JSON."""
    contacts = list(Contact.objects.values('id', 'nom', 'email', 'message'))
    return JsonResponse({'contacts': contacts})


# Gardé pour compatibilité / rendu de page simple
# (mais non utilisé dans le flux AJAX actuel)
def getContact(request):
    return render(request, "app/index.html")