from random import choice
import json
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User
from django.core.serializers import json
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.template.loader import render_to_string
from crm_manager.forms import PromocodeForm, CalculatorForm, CodeForm
from crm_manager.models import Promocode, Calculator, Code
from django.views.generic import View
from django.http import HttpResponse, response, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime

# Create your views here.

class PromoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.obj = Promocode.objects.all().order_by("-id")
        return super(PromoView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'promo.html', {"obj": self.obj})

    def post(self, request):
        print "promo list"
        return render(request, 'partial/promo_list.html', {"obj": self.obj})

class AddPromo(View):
    def post(self, request):
        print "Add promocode"
        form = PromocodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('promo')
        return render(request, 'add_promo.html', {'form': form})

    def get(self, request):
        form = PromocodeForm()
        template = render(request, 'add_promo.html', {'form': form})
        return template

class Landing(View):
    def get(self, request):
        return render(request, "landing.html", {})

class CalculatorUpdateView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.obj = Calculator.objects.all().order_by("-id")
        return super(CalculatorUpdateView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = CalculatorForm()
        return render(request, 'partial/cal_list.html', {"obj": self.obj,"form":form})

class CalculatorView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.obj = Calculator.objects.all().order_by("-id")
        return super(CalculatorView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = CalculatorForm()
        return render(request, 'calculator.html', {"obj": self.obj,"form":form})

    def post(self, request):
        num1 = int(request.POST.get("firstnumber"))
        print num1
        num2 = int(request.POST.get("lastnumber"))
        print num2
        type = request.POST.get("type")
        print type
        result = request.POST.get("Result")
        # print "result is",result
        user = request.POST.get("user")
        # print user
        result=0

        if type == '+':
            result=num1+num2

        elif type == '-':
            result=num1-num2

        elif type == '*':
            result=num1*num2

        elif type == '/':
            result=float((num1)/ float (num2))
        else:
            print("Invalid input")
        print "result is ", result


        try:
            cal = Calculator.objects.create(firstnumber=num1,
                                            lastnumber=num2,
                                            result=result,
                                            type=type,
                                            user_id=user,
                                            )
        except Exception as e:
            print e
        return HttpResponse(result)


class EditCalculatorView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.obj = Calculator.objects.all().order_by("-id")
        return super(EditCalculatorView, self).dispatch(request, *args, **kwargs)

    def get(self, request,id):
        form = CalculatorForm()
        return render(request, 'edit_cal.html', {"obj": self.obj, "form": form})

    def post(self, request):
        print request.POST
        num1 = int(request.POST.get("firstnumber"))
        print num1
        num2 = int(request.POST.get("lastnumber"))
        print num2
        type = request.POST.get("type")
        print type
        result = request.POST.get("Result")
        # print "result is",result
        user = request.POST.get("user")
        # print user
        result = 0

        if type == '+':
            result = num1 + num2

        elif type == '-':
            result = num1 - num2

        elif type == '*':
            result = num1 * num2

        elif type == '/':
            result = float((num1) / float(num2))
        else:
            print("Invalid input")
        print "result is ", result

        try:
            cal = Calculator.objects.get(id=id)
        except Exception as e:
            print e
        return HttpResponse(result)

1


class AddCodeView(CreateView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AddCodeView, self).dispatch(request, *args, **kwargs)

    form_class = CodeForm
    model = Code
    template_name = 'add_code.html'
    success_url = "list_data.html"

    def form_invalid(self, form):
        response = super(AddCodeView, self).form_invalid(form)
        if self.request.is_ajax():
            print(form.cleaned_data)
            print "Field Required"
            print self.request.is_ajax()
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AddCodeView, self).form_valid(form)
        if self.request.is_ajax():
            if form.is_valid():
                self.object = form.save()
            if form.is_valid():
                print "Valid Form"
            print "save form"
            data = {
                'id': self.object.id,
            }
            print data
            return JsonResponse(data)
        else:
            return response

class ListData(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.obj = Code.objects.all().order_by("-id")
        return super(ListData, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form =CodeForm
        return render(request, 'list_data.html', {"obj": self.obj,"form":form})

    def post(self, request):
        form = CodeForm
        return render(request, 'list_data.html', {"obj": self.obj, "form": form})



class Detail(DetailView):
    model = Code
    template_name = "detail_view.html"
    def get_object(self, id=id):
        if self.request.is_ajax():
            id_=self.kwargs.get("id")
        return get_object_or_404(Code, id=id_)



class Edit(UpdateView):
        form_class = CodeForm
        model = Code

        def form_valid(self, form):

            if self.request.is_ajax():
                self.object = form.save()
                return HttpResponse(json.dumps("success"),
                                    mimetype="application/json")
            return super(Edit, self).form_valid(form)

        def form_invalid(self, form):
            if self.request.is_ajax():
                return HttpResponseBadRequest(json.dumps(form.errors),
                                              mimetype="application/json")
            return super(Edit, self).form_invalid(form)


class UpdateListView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.obj = Code.objects.all().order_by("-id")
        return super(UpdateListView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = CalculatorForm()
        return render(request, 'partial/partial_list_data.html', {"obj": self.obj,"form":form})


class UpdateCodeView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.obj = Code.objects.all().order_by("-id")
        return super(UpdateCodeView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = CalculatorForm()
        return render(request, 'partial/partial_list_data.html', {"obj": self.obj,"form":form})

    def post(self,request):
        id = request.GET['id']
        print id
        code = get_object_or_404(Code, id=id)
        form = CodeForm(initial={
            'name': code.name,
            'email': code.email,
            'phone': code.phone,
            'age': code.age,
        })
        context = {'form': form}
        string = render_to_string('partial/edit_data_form.html', context)
        return HttpResponse(string)

class Delete(DeleteView):
    model = Code
    success_url = reverse_lazy("list_data")


