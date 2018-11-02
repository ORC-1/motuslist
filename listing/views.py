from django.views.generic import ListView
from django.shortcuts import render
from . models import Listing,Asset, Categories
from .filters import searchbox


# Create your views here.
class HomeView(ListView):
    context_object_name = 'Lists'
    template_name = 'index.html'
    queryset  = Listing.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['Asset'] = Asset.objects.all().order_by('-id')
        context['Cat'] = Categories.objects.all().order_by('-id')


        return context


class Travel(ListView):
    context_object_name = 'Lists'
    template_name = 'Travel.html'
    queryset  = Listing.objects.filter(Category="2")

    def get_context_data(self, **kwargs):
        context = super(Travel, self).get_context_data(**kwargs)
        context['Travel'] = Categories.objects.filter(category="Travel")


        return context

class Art(ListView):
    context_object_name = 'Lists'
    template_name = 'Art.html'
    queryset  = Listing.objects.filter(Category="4")

    def get_context_data(self, **kwargs):
        context = super(Art, self).get_context_data(**kwargs)
        context['Art'] = Categories.objects.filter(category="Art")


        return context

class Book_Shop(ListView):
    context_object_name = 'Lists'
    template_name = 'Book_Shop.html'
    queryset  = Listing.objects.filter(Category="4")

    def get_context_data(self, **kwargs):
        context = super(Book_Shop, self).get_context_data(**kwargs)
        context['Book_Shop'] = Categories.objects.filter(category="Book_Shop")


        return context


class Restaurants(ListView):
    context_object_name = 'Lists'
    template_name = 'Restaurants.html'
    queryset  = Categories.objects.filter(category=3)

    def get_context_data(self, **kwargs):
        context = super(Restaurants, self).get_context_data(**kwargs)
        context['Restaurants'] = Categories.objects.filter(category=3)


        return context

class Business(ListView):
    context_object_name = 'Lists'
    template_name = 'Business.html'
    queryset  = Listing.objects.filter(Category=2)

    # def get_context_data(self, **kwargs):
    #     context = super(Business, self).get_context_data(**kwargs)
    #     context['Business'] = Listing.objects.filter(Category=3)
    #
    #
    #     return context

# SEARCH FIELD HANDLER
def search(request):
    List = Listing.objects.all()
    search = searchbox(request.GET, queryset=List)
    return render(request, 'searchT.html', {'filter': search})
