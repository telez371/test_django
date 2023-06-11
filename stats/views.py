from django.db.models import Count, Avg, Q
from rest_framework import generics
from .models import Site, Action
from .serializers import SiteSerializer, ActionSerializer


class SiteList(generics.ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer




class ActionList(generics.ListCreateAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class ActionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class SiteSearch(generics.ListAPIView):
    serializer_class = SiteSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        min_unique_users = int(self.request.query_params.get('min_unique_users', 0))
        max_unique_users = int(self.request.query_params.get('max_unique_users', float('inf')))
        min_purchases = int(self.request.query_params.get('min_purchases', 0))
        max_purchases = int(self.request.query_params.get('max_purchases', float('inf')))
        min_avg_purchases = float(self.request.query_params.get('min_avg_purchases', 0))
        max_avg_purchases = float(self.request.query_params.get('max_avg_purchases', float('inf')))

        queryset = Site.objects.annotate(
            unique_users=Count('action__user_id', distinct=True),
            total_purchases=Count('action', filter=Q(action_type='purchase')),
            avg_purchases=Avg('action__purchased_items', filter=Q(action_type='purchase'))
        ).filter(
            action__timestamp__date__range=[start_date, end_date],
            unique_users__gte=min_unique_users,
            unique_users__lte=max_unique_users,
            total_purchases__gte=min_purchases,
            total_purchases__lte=max_purchases,
            avg_purchases__gte=min_avg_purchases,
            avg_purchases__lte=max_avg_purchases
        ).distinct()

        return queryset
