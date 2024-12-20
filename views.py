from django.shortcuts import render
from django.views import generic
from.models import Item, TYPE, DRINK_TYPES, MEAL_TYPES

# Each class is one side in the app


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Kombiniere TYPE, MEAL_TYPES und DRINK_TYPES in einem Dictionary
        context["items"] = {
            "types": TYPE,
            "meal_types": MEAL_TYPES,
            "drink_types": DRINK_TYPES,
            "all_items": Item.objects.all()
        }
        return context


class MenuItemDetail(generic.DetailView):  # good for detail view
    model = Item
    template_name = "menu_item_detail.html"
