from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import OrderForm, CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only

import itertools




# Create your views here.

@unauthenticated_user
def registerpage(request):

    form = CreateUserForm()

    if request.method == "POST": 
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username= form.cleaned_data.get('username')

            group=Group.objects.get(name='players')
            user.groups.add(group)
            Player.objects.create(user=user)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context={'form': form}
    return render(request,'gametime/register.html', context)

@unauthenticated_user
def loginpage(request):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('PlayerProf')

        else:
            messages.info(request, 'Username OR Password is incorrect')
            

    context={}
    return render(request,'gametime/login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
@admin_only
def home(request):
    booking=Booking.objects.all()
    return render(request,'gametime/dashboard.html')

@login_required(login_url='login')
def Schedgames(request):
    schedules =  Schedule.objects.all()



    # print(schedules)
    # first = schedules[0]
    # firstsched=first.booking_set.all()
    # print(firstsched)
    # firstbook=firstsched[1]
    # print(firstbook)

    # get_all_scheds = schedules.count()
    # print(get_all_scheds)

    # first_sched = firstsched.first()
    # print(first_sched)
    # id_first = first_sched.first()
    # id_firsts = id_first.id()

    # def get_matchups(*something)

    # youw = all_scheds[0]
    # print(youw)

    all_scheds=[]
    for cutie in range(len(schedules)):
        all_scheds.append(schedules[cutie])
    
    index_all_scheds = len(all_scheds)
    # print(index_all_scheds)






    # goods to
    # print(len(all_scheds))
    # kiss= all_scheds[1].booking_set.all()[0]
    # for i in kiss:
    #     print(i.player)

    # perfect algo
    # print(len(all_scheds))
    # kiss= all_scheds[3].booking_set.all()
    # print(kiss)
    # for i in kiss:
    #     print(i.player)

    
    # per_sched_booking = []
    # for sched in range(len(all_scheds)):
    #     per_sched_booking.append(all_scheds[sched])

    # print(len(per_sched_booking))

    # kissy = per_sched_booking.booking_set.all()


    # for j in kissy:
    #     print(j.player)

    
        # print(all_sched.count())
        # for i in all_sched:
        #     print(i.date_booked)

    # for cutie in range(len(schedules)):
    #     all_sched=schedules[cutie]
    #     for count in all_sched:
    #         per_sched= all_sched[count].booking_set.all()
    #         print(per_sched)

        # print(all_sched.count())
        # for i in all_sched:
        #     print(i.date_booked)



    
        
    # for count in range(len(all_sched)):
    #     per_sched=schedules[count].booking_set.all()
    #     print(per_sched)
    #     print(per_sched.count())
        
        
    # scheds = Schedule.objects.get(id=pk)

    return render(request,'gametime/schedules.html', {'schedules': schedules})

@login_required(login_url='login')
@allowed_users(allowed_roles=['players'])
def PlayerProf(request):

    playerr = request.user.player.booking_set.all()

    print('BOOKINGS: ', playerr)

    totalbooking=playerr.count()


@allowed_users(allowed_roles=['players','admin'])
def PlayerProf(request):

    playerr = request.user.player.booking_set.all()
    totalbooking=playerr.count()

    context = {'playerr':playerr, 'totalbooking': totalbooking}
    return render(request,'gametime/profile.html', context)

@login_required(login_url='login')
def createbooking(request):

    form = OrderForm()
    if request.method == "POST":
        # print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PlayerProf')

    context = {'form': form}

    return render(request,'gametime/booking_form.html', context)

@login_required(login_url='login')
def updatebooking(request, pk):


    book = Booking.objects.get(id=pk)
    form = OrderForm(instance=book)
    if request.method == "POST":
        # print('Printing POST:', request.POST)
        form = OrderForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form': form}
    return render(request,'gametime/booking_form.html', context)

@login_required(login_url='login')
def deletebooking(request, pk):

    book = Booking.objects.get(id=pk)
    

    if request.method == "POST":
        book.delete()
        return redirect('PlayerProf')

    context= {'booking': book}
    return render(request, 'gametime/delete.html', context)




@login_required(login_url='login')
def matchups(request,pk_tests):
    books=Booking.objects.filter(schedule=pk_tests)
    booky=books[0:5]
    booky2=books[6:11]

    boks=books.first()

def matchups(request):
    schedules =  Schedule.objects.all()


    # list of schedules e.g Eastwood Ph1 (August 21, 2022) (5:00PM-6:00PM)
    all_scheds=[]
    for cutie in range(len(schedules)):
        all_scheds.append(schedules[cutie])
    

    my_dict = dict() 
    for index,value in enumerate(all_scheds):
        my_dict[index] = value.booking_set.all()


    myfinal_list=[]
    for sched in range(len(my_dict)):
        myfinal_list.append(my_dict.get(sched))

    print(myfinal_list)
   




    # print(my_dict.get(0).count())
    # print(my_dict.get(1).count())
    # print(my_dict.get(2).count())
    # print(my_dict.get(3).count())

    # index_all_scheds = len(all_scheds)
    # # print(index_all_scheds)

    # per_sched=[]
    # for sched in range(len(all_scheds)):
    #     per_sched.append(all_scheds[sched])
        

    

    # youw = all_scheds[0].booking_set.all()[0:4]
    # for i in youw:
    #     print(i.date_booked)


    # for i in all_scheds[0]:
    #     print()
    # allbookings = Booking.objects.all()

    # courts=['Eastwood Ph1','Eastwood Ph2','Diliman','Eastwind', 'Centella']
    # time=['5:00PM-6:00PM','6:00PM-7:00PM','7:00PM-8:00PM', '8:00PM-9:00PM']
    # hey = Booking.objects.all()
    # print(hey)

    # orderbysched = Booking.objects.order_by('schedule')
    # byname = orderbysched.first()
    # print(byname)
    # bynamedetails = byname.schedule.court
    # print(bynamedetails)
    # bydate = byname.schedule.date
    # print(bydate)
    # bytime = byname.schedule.schedule
    # print(bytime)


    
    
    cencourt1=Booking.objects.filter(schedule__court='Centella').filter(schedule__date='August 23, 2022').filter(schedule__schedule='7:00PM-8:00PM')
    
    
    cenTeam1=cencourt1[0:5]
    cenTeam2=cencourt1[6:11]
    centtitle=cencourt1.first()

    cencourt2=Booking.objects.filter(schedule__court='Centella').filter(schedule__date='August 26, 2022').filter(schedule__schedule='5:00PM-6:00PM')
    
    
    cen2Team1=cencourt2[0:5]
    cen2Team2=cencourt2[6:11]
    cent2title=cencourt2.first()

    # cencourt3=Booking.objects.filter(schedule__court='Centella').filter(schedule__date='August 23, 2022').filter(schedule__schedule='7:00PM-8:00PM')
    
    
    # cen3Team1=cencourt[0:5]
    # cen3Team2=cencourt[6:11]
    # cent3title=books.first()

    # cencourt4=Booking.objects.filter(schedule__court='Centella').filter(schedule__date='August 23, 2022').filter(schedule__schedule='7:00PM-8:00PM')
    
    
    # cen4Team1=cencourt[0:5]
    # cen4Team2=cencourt[6:11]
    # cent4title=books.first()


    # cencourt5=Booking.objects.filter(schedule__court='Centella').filter(schedule__date='August 23, 2022').filter(schedule__schedule='7:00PM-8:00PM')



    # cen5Team1=cencourt[0:5]
    # cen5Team2=cencourt[6:11]
    # cent5title=books.first()

    ephOneCourt1=Booking.objects.filter(schedule__court='Eastwood Ph1').filter(schedule__date='August 21, 2022').filter(schedule__schedule='5:00PM-6:00PM')

    ephOneTeam1=ephOneCourt1[0:5]
    ephOneTeam2=ephOneCourt1[6:11]
    ephOnetitle=ephOneCourt1.first()



    DilCourt1=Booking.objects.filter(schedule__court='Diliman').filter(schedule__date='August 24, 2022').filter(schedule__schedule='6:00PM-7:00PM')

    DilTeam1=DilCourt1[0:5]
    DilTeam2=DilCourt1[6:11]
    Diltitle=DilCourt1.first()


    DilCourt2=Booking.objects.filter(schedule__court='Diliman').filter(schedule__date='August 25, 2022').filter(schedule__schedule='8:00PM-9:00PM')

    Dil2Team1=DilCourt2[0:5]
    Dil2Team2=DilCourt2[6:11]
    Dil2title=DilCourt2.first()



    ewdCourt1=Booking.objects.filter(schedule__court='Eastwind').filter(schedule__date='August 22, 2022').filter(schedule__schedule='7:00PM-8:00PM')
    
    ewdTeam1=ewdCourt1[0:5]
    ewdTeam2=ewdCourt1[6:11]
    ewdtitle=ewdCourt1.first()

    # books=Booking.objects.filter(schedule__court='Eastwood Ph2').filter(schedule__date='August 23, 2022').filter(schedule__schedule='7:00PM-8:00PM')
    # books=Booking.objects.filter(schedule__court='Diliman').filter(schedule__date='August 23, 2022').filter(schedule__schedule='7:00PM-8:00PM')
    # books=Booking.objects.filter(schedule__court='Eastwind').filter(schedule__date='August 23, 2022').filter(schedule__schedule='7:00PM-8:00PM')
    # books=Booking.objects.filter(schedule__court='Eastwind').filter(schedule__date='August 23, 2022').filter(schedule__schedule='7:00PM-8:00PM')


    
    
    # get schedule date

    # context = {'books':books, 'boks':boks, 'booky':booky, 'booky2':booky2}

    context = {'cencourt1':cencourt1,
               'cenTeam1':cenTeam1, 
               'cenTeam2':cenTeam2, 
               'centtitle':centtitle,

               'cencourt2':cencourt2,
               'cen2Team1':cen2Team1, 
               'cen2Team2':cen2Team2, 
               'cent2title':cent2title,

               'ephOneCourt1':ephOneCourt1,
               'ephOneTeam1':ephOneTeam1, 
               'ephOneTeam2':ephOneTeam2, 
               'ephOnetitle':ephOnetitle,


               'DilCourt1':DilCourt1,
               'DilTeam1':DilTeam1, 
               'DilTeam2':DilTeam2, 
               'Diltitle':Diltitle,


               'DilCourt2':DilCourt2,
               'Dil2Team1':Dil2Team1, 
               'Dil2Team2':Dil2Team2, 
               'Dil2title':Dil2title,


               'ewdCourt1':ewdCourt1,
               'ewdTeam1':ewdTeam1, 
               'ewdTeam2':ewdTeam2, 
               'ewdtitle':ewdtitle,


               # 'cencourt1':cencourt1,
               # 'boks':boks, 
               # 'booky':booky, 
               # 'booky2':booky2,


               # 'cencourt1':cencourt1,
               # 'boks':boks, 
               # 'booky':booky, 
               # 'booky2':booky2,


               # 'cencourt1':cencourt1,
               # 'boks':boks, 
               # 'booky':booky, 
               # 'booky2':booky2,


               # 'cencourt1':cencourt1,
               # 'boks':boks, 
               # 'booky':booky, 
               # 'booky2':booky2,
               'myfinal_list': myfinal_list,
               'all_scheds': all_scheds}


    return render(request,'gametime/matchups.html', context)