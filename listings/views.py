from django.shortcuts import render ,redirect
from . models  import Listings , ContactMessage
from django.shortcuts import render, get_object_or_404
from .models import Listings
from django.core.paginator import Paginator



# home page 
def home(request):
    listings = Listings.objects.all()[:6]
    property_counts = {
        'appartment': Listings.objects.filter(type_bien__icontains='appartment').count(),
        'villa': Listings.objects.filter(type_bien__icontains='villa').count(),
        'home': Listings.objects.filter(type_bien__icontains='home').count(),
        'bureau': Listings.objects.filter(type_bien__icontains='bureau').count(),
        'building': Listings.objects.filter(type_bien__icontains='building').count(),
        'townhouse': Listings.objects.filter(type_bien__icontains='townhouse').count(),
        'shop': Listings.objects.filter(type_bien__icontains='shop').count(),
        'garage': Listings.objects.filter(type_bien__icontains='garage').count(),
    }

    # Obtenir les adresses et types de biens distincts
    addresses = Listings.objects.values_list('Adresse', flat=True).distinct()
    types_bien = Listings.objects.values_list('type_bien', flat=True).distinct()

    context = {
        'listings': listings,
        'property_counts': property_counts,
        'addresses': addresses,
        'types_bien': types_bien
    }
    return render(request, 'index.html', context)


# about page 
def about(request):
    return render(request, 'about.html')

# contact page
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            data = ContactMessage(name=name, email=email, subject=subject, message=message)
            data.save()
            return render(request, 'contact.html', {'success': 'Message sent successfully'})
        else:
            return render(request, 'contact.html', {'error': 'All fields are required'})

    return render(request, 'contact.html')


# list of property page
def PropertyList(request):
    listings = Listings.objects.all()
    paginator = Paginator(listings, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Obtenir les adresses et types de biens distincts
    addresses = Listings.objects.values_list('Adresse', flat=True).distinct()
    types_bien = Listings.objects.values_list('type_bien', flat=True).distinct()

    return render(request, 'property-list.html', {
        'page_obj': page_obj,
        'active_tab': 'featured',
        'addresses': addresses,
        'types_bien': types_bien
    })


# list type of properties page
def PropertyType(request):
    property_counts = {
        'appartment': Listings.objects.filter(type_bien__icontains='appartment').count(),
        'villa': Listings.objects.filter(type_bien__icontains='villa').count(),
        'home': Listings.objects.filter(type_bien__icontains='home').count(),
        'bureau': Listings.objects.filter(type_bien__icontains='bureau').count(),
        'building': Listings.objects.filter(type_bien__icontains='building').count(),
        'townhouse': Listings.objects.filter(type_bien__icontains='townhouse').count(),
        'shop': Listings.objects.filter(type_bien__icontains='shop').count(),
        'garage': Listings.objects.filter(type_bien__icontains='garage').count(),
    }
    return render(request, 'property-type.html', {'property_counts': property_counts})


# display  each of type of property 
def properties_by_type(request, property_type):
    properties = Listings.objects.filter(type_bien__icontains=property_type)
    return render(request, 'properties_by_type.html', {'properties': properties, 'type_bien': property_type})

# agent property page
def PropertyAgent(request):
    return render(request, 'property-agent.html') 

# Testimonial page
def Testimonial(request):
    return render(request, 'testimonial.html') 

# search section for property list page
def property_search(request):
    if request.method == 'POST':
        action_commerciale = request.POST.get('action_commerciale')
        type_bien = request.POST.get('type_bien')
        location = request.POST.get('location')
        print(f"Action commerciale: {action_commerciale}, Type de bien: {type_bien}, Location: {location}")  
        results = Listings.objects.filter(
            Action_commerciale=action_commerciale,
            type_bien__icontains=type_bien,
            Adresse__icontains=location  
        )
        print(f"Nombre de résultats trouvés: {results.count()}") 
        return render(request, 'property-list.html', {'results': results})
    return render(request, 'search_form.html')

# search section for home page
def property_search2(request):
    if request.method == 'POST':
        action_commerciale = request.POST.get('action_commerciale')
        type_bien = request.POST.get('type_bien')
        location = request.POST.get('location')
        print(f"Action commerciale: {action_commerciale}, Type de bien: {type_bien}, Location: {location}")  
        results = Listings.objects.filter(
            Action_commerciale=action_commerciale,
            type_bien__icontains=type_bien,
            Adresse__icontains=location  
        )
        print(f"Nombre de résultats trouvés: {results.count()}")  
        return render(request, 'search_results.html', {'results': results})
    return render(request, 'search_form.html')


# list of sale properties
def property_list_for_sale(request):
    listings = Listings.objects.filter(Action_commerciale='vendre')
    paginator = Paginator(listings, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'property-list.html', {'page_obj': page_obj, 'active_tab': 'for_sale'})

# Vue pour la liste des biens à louer
def property_list_for_rent(request):
    listings = Listings.objects.filter(Action_commerciale='louer')
    paginator = Paginator(listings, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'property-list.html', {'page_obj': page_obj, 'active_tab': 'for_rent'})

# announce details page 
def annonce_detail(request, id):
    annonce = get_object_or_404(Listings, id=id)
    return render(request, 'annonce_detail.html', {'annonce': annonce})




