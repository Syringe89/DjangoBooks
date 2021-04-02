import stripe
from django.contrib.auth.models import Permission
from django.shortcuts import render
from django.views.generic import TemplateView

from bookstore_project import settings

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class OrdersPageView(TemplateView):
    template_name = 'purchase.html'

    def get_context_data(self, **kwargs):
        context = super(OrdersPageView, self).get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


def charge(request):
    permission = Permission.objects.get(codename='special_status')
    user = request.user
    user.user_permissions.add(permission)

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST.get('stripeToken')
        )
        print(charge)
    return render(request, 'charge.html')
