from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Max


# Create your views here.
def index(request):
    return render(request,'/gbs_app/index.html')


def uhome(request):
    return render(request, './gbs_app/uhome.html')


def u_details(request):
    return render(request, './gbs_app/u_details.html')


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        ul = userlogin.objects.filter(username=username, password=password, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].username
            request.session['user_id'] = ul[0].id
            context1 = {'uname': request.session['user_name']}
            return render(request,'./gbs_app/homepage.html',context1)
        else:
            msg = '<h3> Invalid Username or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './gbs_app/index.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './gbs_app/index.html',context)


def homepage(request):
    return render(request,'./gbs_app/homepage.html')


def register(request):
    return render(request,'./gbs_app/register.html')


def staff(request):
    return render(request,'./gbs_app/staff.html')


def user(request):
    return render(request,'./gbs_app/user.html')


def book(request):
    return render(request, './gbs_app/book.html')


def shome(request):
    return render(request, './gbs_app/shome.html')


def update(request):
    return render(request, './gbs_app/update.html')

from .models import user_details


def user_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('date')
        address = request.POST.get('address')
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        usertype = request.POST.get('usertype')
        uname=mail
        utype = usertype

        if userlogin.objects.filter(username=uname):
            msg = {'msg1': 'Email Already Exist!!'}
            return render(request, './gbs_app/register.html', msg)
        else:

            ul = userlogin(username=uname, password=password,u_type=usertype)
            ul.save()
            user_id = userlogin.objects.all().aggregate(Max('id'))['id__max']

            ud = user_details(user_id=user_id,name=name, date_of_birth=dob, address=address, mail=mail, mobile_no=phone, usertype=usertype, u_password=password)
            ud.save()

            print(user_id)
            context = {'msg': 'User Registered'}
            return render(request, 'gbs_app/register.html', context)

    else:
        return render(request, 'gbs_app/register.html')


def user_del(request):
    id = request.GET.get('id')
    u = user_details.objects.get(user_id=int(id))
    u.delete()

    l = userlogin.objects.get(id=int(id))
    l.delete()

    details = user_details.objects.all()
    d = {'user': details}
    return render(request, './gbs_app/u_details.html', d)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        ul = userlogin.objects.filter(username=username, password=password, u_type='user')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].username
            request.session['user_id'] = ul[0].id
            return render(request,'./gbs_app/uhome.html')
        else:
            msg = '<h3> Invalid Username or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './gbs_app/user.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './gbs_app/user.html',context)


def staff_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        ul = userlogin.objects.filter(username=username, password=password, u_type='staff')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].username
            request.session['user_id'] = ul[0].id
            return render(request,'./gbs_app/shome.html')
        else:
            msg = '<h3> Invalid Username or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './gbs_app/staff.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './gbs_app/staff.html',context)


from .models import gasrefill_booking


def book_refill(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        cylinder = request.POST.get('cylinder')

        ud = gasrefill_booking(name=name,email=email,date=date,time=time,cylinder=cylinder)
        ud.save()
        context = {'msg':'Refill Requested'}
        return render(request, './gbs_app/book.html',context)
    else:
        return render(request, './gbs_app/book.html')


def user_details_update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        up = user_details.objects.get(id=int(id))

        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        usertype = request.POST.get('usertype')
        address = request.POST.get('address')
        mobile_no = request.POST.get('mobile_no')
        mail = request.POST.get('mail')

        up.name = name
        up.date_of_birth = date_of_birth
        up.usertype = usertype
        up.mobile_no = mobile_no
        up.address = address
        up.mail = mail

        up.save()

        context = {'msg': 'User Details Updated','up':up}
        return render(request, 'gbs_app/update.html',context)

    else:
        id = request.GET.get('id')
        up = user_details.objects.get(id=int(id))
        context={'up':up}
        return render(request, 'gbs_app/update.html',context)


def retrive_user_details(request):
    details = user_details.objects.all()
    d ={'user': details }
    return render(request,'./gbs_app/u_details.html',d)


def retrive_view_booking(request):
    details = gasrefill_booking.objects.all()
    d ={'gas': details }
    return render(request,'./gbs_app/view_booking.html',d)


def logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return index(request)
    else:
        return index(request)