from django import views
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Phone, Trademark
from .forms import PhoneForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PhoneList(ListView):
    paginate_by = 5
    model = Phone
    queryset = Phone.objects.order_by('-time_publish')
    print(queryset[0].id)

    def get_context_data(self, **kwargs):
        queryset = Phone.objects.order_by('-time_publish')
        context = super(PhoneList, self).get_context_data(**kwargs)
        context['id1'] = queryset[0].id
        context['id2'] = queryset[1].id
        context['trademark_list'] = Trademark.objects.all()
        context['count'] = len(Phone.objects.all())
        return context


class Trademark_List(ListView):
    model = Trademark
    template_name = 'Phone/base.html'

    def get_context_data(self, **kwargs):
        context = super(Trademark_List, self).get_context_data(**kwargs)
        context['trademark_list'] = Trademark.objects.all()
        context['count'] = len(Phone.objects.all())
        return context


class PhoneView(DetailView):
    model = Phone


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class PhoneCreate(AjaxableResponseMixin, CreateView):
    model = Phone
    fields = ['name', 'trademark', 'image', 'price', 'description']
    success_url = reverse_lazy('Phone:phone_list')


class PhoneUpdate(UpdateView):
    model = Phone
    fields = ['name', 'trademark', 'image', 'price', 'description']
    success_url = reverse_lazy('Phone:phone_list')


class PhoneDelete(DeleteView):
    model = Phone
    success_url = reverse_lazy('Phone:phone_list')


class SearchResultsView(ListView):
    model = Phone
    template_name = 'phone_list.html'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Phone.objects.filter(
            Q(name__contains=query)
        ).order_by("-time_publish")
        print(query)
        return object_list

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['trademark_list'] = Trademark.objects.all()
        context['count'] = len(Phone.objects.all())
        return context


class TrademarkResultView(ListView):
    model = Phone
    template_name = 'phone_list.html'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('trademark')
        object_list = Phone.objects.filter(
            Q(trademark__name__contains=query)
        ).order_by("-time_publish")
        return object_list

    def get_context_data(self, **kwargs):
        context = super(TrademarkResultView, self).get_context_data(**kwargs)
        context['trademark_list'] = Trademark.objects.all()
        context['count'] = len(Phone.objects.all())
        return context
