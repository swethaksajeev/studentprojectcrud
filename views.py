from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.views import View
from django.http import JsonResponse
from app.models import Student

class StudentList(View):
    def get(self,request):
        # data=[{'name':'arun','age':23,'course':'python','marks':45},
        #       {'name':'kiran','age':22,'course':'java','marks':50}]

        s=list(Student.objects.all().values()) #read all data records student table
        print(s)
        print(type(s)) #queryset of objects

        return JsonResponse(s,safe=False)

#queryset -->python native -->json

# class StudentDetails(View):
#     def get(self,request):
#         data1={'name':'arun','age':23,'course':'python','marks':45}
#         return JsonResponse(data1)

#apiview creating a new student record

from json import loads
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name="dispatch")

class StudentCreate(View):
    def post(self,request):
        #fetch data from client side
        form_data=request.body #json data


        #convert json into python native type(dictionary)
        data=loads(form_data)
        print(data)
        n=data['name']
        a=data['age']
        m=data['marks']
        c=data['course']
        #creates a new record inside db table
        #insert into student(name,age,course,marks)values(%s,%s,%s,%s),(n,a,c,m))
        #orm query
        #modelname.objects.create(field=value,field=value,....)

        s=Student.objects.create(Name=n,Age=a,Course=c,Marks=m)
        s.save()

        #returns response

        return JsonResponse({'message':'created'})

#api view for reading specific record
class StudentDetails(View):
    def get(self,request,i):
        print(i)

        #reads data from student table matching with id i(modelobject)
        s=Student.objects.filter(id=i)
        print(s)
        print(type(s))
        #converts the data into python native type

        data=list(s.values())
        print(data)
        print(type(data))
        return JsonResponse(data,safe=False)

#api view for deleting existing record

@method_decorator(csrf_exempt,name="dispatch")
class StudentDelete(View):
    def delete(self,request,i):
        #fetch the data from student table

        s=Student.objects.get(id=i)

        #delete the record

        s.delete()

        #send response back to client
        return JsonResponse({'message':'deleted'})