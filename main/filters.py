import django_filters
from .models import Event


class EventsFilter(django_filters.FilterSet):
    from_date = django_filters.IsoDateTimeFilter(field_name='date', lookup_expr='gte')
    to_date = django_filters.IsoDateTimeFilter(field_name='date', lookup_expr='lte')
    types = django_filters.CharFilter(field_name='types', lookup_expr='in')

    class Meta:
        model = Event
        fields = ['from_date', 'to_date', 'types']


# class EventDeleteFilter(django_filters.FilterSet):
