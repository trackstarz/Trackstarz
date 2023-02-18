from django.urls import path

from .views import (
    MembershipSelectView,
    PaymentView,
    updateTransactions,
    profile_view,
    cancelSubscription,
)

app_name = 'memberships'

urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('update-transactions/<subscription_id>/', updateTransactions, name='update-transactions'),
    path('profile/', profile_view, name='profile'),
    path('cancel/', cancelSubscription, name='cancel'),
]
