from rest_framework.pagination import PageNumberPagination


class MyPagenation(PageNumberPagination):
    page_size = 30