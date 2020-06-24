import django_filters

from django_filters import DateFilter,CharFilter

from .models import application,university

class appfilter(django_filters.FilterSet):
    st_dt  =  DateFilter(field_name="datetime",lookup_expr='gte')
    en_dt  = DateFilter(field_name="datetime",lookup_expr='lte')
    user = CharFilter(field_name="user" ,lookup_expr="icontains")
    firstname = CharFilter(field_name="firstname" ,lookup_expr="icontains")


    class Meta:
        model=application
        fields='__all__'
        exclude=['dob','datetime','lastname','city','file1','file2']


class unifilter(django_filters.FilterSet):
    location = CharFilter(field_name="loc" ,lookup_expr="icontains")

    class Meta:
        model=university
        fields=['loc']

