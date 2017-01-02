from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import time
import random
import json
import hashlib
from login.models import AuthCode
from login.models import Auth

def default(request):
    return HttpResponse(u'home..')

def index(request):
    return HttpResponse(u'index!')

@csrf_exempt
def login(request):
    data = 'bad request...'
    if request.method == 'GET':
        create_time = time.time()
        random_code = make_random()
        new_auth_code = Auth(create_time=create_time, random_code=random_code)
        new_auth_code.save()
        s = u'login! create_time: %s , your authcode is %s' % (create_time, random_code)
        return HttpResponse(json.dumps(s), content_type='application/json')
    elif request.method == 'POST':
        receive_auth_code = request.POST.get('auth_code', None)
        if not receive_auth_code:
            data = '1'
            return HttpResponse(data)
        xx = Auth.objects.filter(random_code=receive_auth_code)
        if len(xx) > 0:
            saved_create_time = float(Auth.objects.get(random_code=receive_auth_code).create_time)
            current_time = time.time()
            t = current_time - saved_create_time
            if t > 3600.0: # 1h = 60s * 60min = 3600s
                data = '2'
                return HttpResponse(json.dumps(data), content_type='application/json')               
            else:
                data = 'good request'
                return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = '3'
            return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        data = '4'
        return HttpResponse(data)
        

        # if not saved_create_time:
        #     currrent_time = time.time()
        # return HttpResponse('a post request..')
    
   
    # return HttpResponse(json.dumps(s))

# def check(request):
    

def make_random():
    md5 = hashlib.md5()
    num = str(random.randint(10, 10000))
    md5.update(num)
    return str(md5.hexdigest())
    # return u'%s' % num
