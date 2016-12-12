from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from django.views.generic import CreateView, DetailView, UpdateView
from models import Employee, CheckIn
from models import Order
from forms import user_form , order_form#, check_In
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

class Index_view(TemplateView):
    template_name='base.html'

class view(TemplateView):
    template_name='base2.html'

class login(TemplateView):
    template_name='login.html'

class register(FormView):
    template_name='registUs.html'
    form_class=user_form
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        user = form.save()
        x = Employee()
        x.user = user
        x.name = form.cleaned_data['name']
        x.is_lineCh = form.cleaned_data['is_lineCh']
        x.is_qtCh = form.cleaned_data['is_qtCh']
        x.is_storage = form.cleaned_data['is_storage']
        x.is_production = form.cleaned_data['is_production']
        x.category = form.cleaned_data['category']
        x.line = form.cleaned_data['line']
        x.save()
        return super (register, self).form_valid(form)

class re_order(FormView):
    template_name='mkorder.html'
    form_class = order_form
    success_url = reverse_lazy('report_orders')

    def form_valid(self, form):
        o = Order()
        o.or_delivery = form.cleaned_data['or_delivery']
        o.or_receive = form.cleaned_data['or_receive']
        o.or_lineCh = form.cleaned_data['or_lineCh']
        o.or_pieces = form.cleaned_data['or_pieces']
        o.or_status = form.cleaned_data['or_status']
        o.save()
        return super (re_order, self).form_valid(form)

class orders_report(ListView):
    template_name = 'ordersRE.html'
    model = Order

# class check(FormView):
    # template_name='check.html'
    # form_class=check_In

    def form_valid(self, form):
        form.instance.ck_Employee = self.request.user
        return super(check, self).form_valid(form)

@login_required
def checks (request):
    context = {}
    a = CheckIn.objects.filter(Employee = request.user.ck_employee)
    if a.exist():
        tipo_I = (a.latest.ck_tipo == 'o')
    else:
        tipo_I = True
    context ['tipo'] = tipo_I
    context ['show'] = 'i' if (tipo_I) else 'o'
    return render (request, 'check.html', context)


'''
@login_required
def Employeein(request, pk):
'''
