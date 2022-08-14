from audioop import reverse
import chunk
import math, json, functools, operator, datetime, threading
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from .models import FormEntry, Resume
from django.views.decorators.cache import cache_control


@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def get_form(request):  

    # if request.method == 'GET' and 'back' in request.session:
    #     print('cookie has been read')
    #     return HttpResponseRedirect('/apply/get_ending/')

    if request.method == 'POST':
        data = request.POST
        email = data['email'] if 'email' in data and data['email'] else ""
        first_name = data['first-name'] if 'first-name' in data and data['first-name'] else ""
        last_name = data['last-name'] if 'last-name' in data and data['last-name'] else ""
        experience = data['experience-level'] if 'experience-level' in data and data['experience-level'] else ""
        visa_status = data['visa-status'] if 'visa-status' in data and data['visa-status'] else "" 
        salary_expect = data['salary-expect'] if 'salary-expect' in data and data['salary-expect'] else ""
        ph_number = data['ph_number'] if 'ph_number' in data and data['ph_number'] else ""
        employment_status = data['employment-status'] if 'employment-status' in data and data['employment-status'] else ""
        gender = data['gender'] if 'gender' in data and data['gender'] else ""
        resume_name = data['resume'] if 'resume' in data and data['resume'] else ""

        print(type(resume_name))
        print(f'resume variable has : {resume_name}')
        print()
        print(request.FILES)

        in_mem_file = request.FILES['resume']
        binary_file_object = in_mem_file.read()
        # recorded_file  = read_in_mem( in_mem_file, in_mem_file.size )

        resume_dict = {
            'file_data_in_bytes' : binary_file_object,
            'file_name' : in_mem_file.name
        }

        resume_entry = Resume(**resume_dict)
        resume_entry.save()

        data_dict = {
            'first_name' : first_name,
            'last_name' : last_name,
            'email_address' : email,
            'experience' : experience, #0,1,2,3
            'visa_status' : visa_status , # 0,1
            'salary_expect' : salary_expect,
            'ph_number' : ph_number,
            'employment_status' :  employment_status,
            'gender' : gender,
            'resume' : resume_entry
        }

        form_entry = FormEntry(**data_dict)
        
        try:
            form_entry.save()
            print("A new Form and Resume entry has been created.")
        except Exception as ex:
            print('Error is', str(ex))

        request.session['back'] = False
        print('cookie has been set')
        return HttpResponseRedirect('/apply/get_ending/')

    return render(request, 'form.html')

def read_in_mem(in_mem_file , file_size):

    # chunk_size = 320    #must be divisible by 8
    # iterations = math.ceil(file_size / chunk_size)

    for chunk in in_mem_file.chunks:
        recorded_file =+ chunk
        print( 'chunk is',chunk)

    return recorded_file


@csrf_exempt
def get_ending(request):
    return render(request, 'ending.html')
  
    # return HttpResponseRedirect('/thanks/')
    