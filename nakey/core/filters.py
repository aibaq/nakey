from django.db.models import Q
from rest_framework.filters import BaseFilterBackend

import coreapi
import coreschema


class CategoryFilter(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [
            coreapi.Field(name='category',
                          schema=coreschema.Boolean(
                              title='category',
                              description='category id'
                          ),
                          required=False,
                          location='query')
        ]

    def filter_queryset(self, request, queryset, view):
        if request.query_params.get('category', '').isdigit():
            category_id = int(request.query_params['category'])
            queryset = queryset.filter(Q(category_id=category_id) | Q(category__parent__id=category_id))
        return queryset
