from django.shortcuts import render

from Region.models import Town


def load_cities(request):
    country_id = request.GET.get('county')
    cities = Town.objects.filter(region_id=country_id).order_by('name')
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
