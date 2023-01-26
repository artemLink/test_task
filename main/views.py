import requests
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from rest_framework import generics, viewsets, status
from .models import Tag, Event
from .serializers import TagSerializer, EventSerializer, EventsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EventsFilter
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core import serializers


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class EventAPIGet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    allowed_methods = ['Get', 'POST', 'PATCH', 'DELETE']

    def create(self, request, *args, **kwargs):
        # Parse tags from request.data
        tags = request.data.get('tags', '').split(';')
        request.data._mutable = True
        request.data['tags'] = tags
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        event = self.get_object()
        if event.category != 'alarm':
            event.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class EventAPIAllEvents(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EventsFilter


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Вітаємо з реєстрацією!')
            return redirect('user_login')
        else:
            messages.error(request, 'Помилка реєстрації')
    else:
        user_form = UserRegisterForm()
    return render(request, './register.html', {'user_form': user_form})


def user_logout(request):
    logout(request)

    return redirect('login')


def main(request):
    return render(request, './index.html')
