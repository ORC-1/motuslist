from . models import Asset, Categories, Listing
import django_filters

class searchbox(django_filters.FilterSet):
    class Meta:
        model = Listing
        fields = ["Name",
                    "Description",
                    "Email",
                    "Phone",
                    "Address",
                    "Website",
                    "Category", ]
