from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter, CharFilter
from .models import Post, Category
from django.forms import DateTimeInput


class PostFilter(FilterSet):
    post_header = CharFilter(
        field_name='post_header',
        lookup_expr='icontains',
        label='Поиск по словам в заголовке',
    )

    post_category = ModelChoiceFilter(
        field_name='post_category',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Любая',
    )

    post_create_date = DateTimeFilter(
        field_name='post_create_date',
        lookup_expr='gt',
        label='Позже даты',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

