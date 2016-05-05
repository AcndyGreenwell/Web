import django_filters
from .models import *


class ResultFilter(django_filters.FilterSet):
    zone_id__zone = django_filters.ModelChoiceFilter()
    datetime_start = django_filters.DateTimeFilter(lookup_expr='gt')
    class Meta:
        model = Results
        fields=['zone_id__zone', 'zone_id', 'datetime_start', 'datetime_end']

    def __init__(self, *args, **kwargs):
        super(ResultFilter, self).__init__(*args, **kwargs)
        filter_=self.filters['zone_id']
        fk_counts = Results.objects.values_list('zone_id').order_by('zone_id').annotate(models.Count('zone_id'))
        zone_ids = [fk for fk,cnt in fk_counts]
        filter_.extra['queryset'] = ZoneOption.objects.filter(pk__in=zone_ids)
        filter_=self.filters['zone_id__zone']
        fk_counts = Results.objects.values_list('zone_id__zone').order_by('zone_id__zone').annotate(models.Count('zone_id__zone'))
        zone_ids = [fk for fk,cnt in fk_counts]
        filter_.extra['queryset'] = Zone.objects.filter(pk__in=zone_ids)