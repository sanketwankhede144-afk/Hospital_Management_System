from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Doctor, Patient, Appointment


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    appointement = Appointment.objects.all()
    
    d = 0;
    p = 0;
    a = 0;
    
    for i in doctor:
        d+=1
    for i in patient:
        p+=1
    for i in appointement:
        a+=1  
    d1 = {'d': d, 'p': p , 'a' : a}

    return render(request, 'index.html',d1)


# ================= ADMIN LOGIN =================

def Login(request):
    error = ""

    if request.method == "POST":

        u = request.POST.get('uname')
        p = request.POST.get('pwd')

        user = authenticate(username=u, password=p)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('home')

        else:
            error = "yes"

    return render(request, 'login.html', {'error': error})


def Logout_admin(request):

    if not request.user.is_staff:
        return redirect('login')

    logout(request)

    return redirect('login')


# ================= DOCTOR =================

def View_doctor(request):

    if not request.user.is_staff:
        return redirect('login')

    doc = Doctor.objects.all()

    return render(request, 'view_doctor.html', {'doc': doc})


def Add_doctor(request):

    if not request.user.is_staff:
        return redirect('login')

    error = ""

    if request.method == "POST":

        n = request.POST.get('name')
        c = request.POST.get('contact')
        sp = request.POST.get('special')

        try:
            Doctor.objects.create(
                name=n,
                mobile=c,
                special=sp
            )

            error = "no"

        except Exception as e:
            print(e)
            error = "yes"

    return render(request, 'add_doctor.html', {'error': error})


def Delete_Doctor(request, pid):

    if not request.user.is_staff:
        return redirect('login')

    try:
        doctor = Doctor.objects.get(id=pid)
        doctor.delete()

    except Doctor.DoesNotExist:
        pass

    return redirect('view_doctor')


# ================= PATIENT =================

def View_Patient(request):

    if not request.user.is_staff:
        return redirect('login')

    pat = Patient.objects.all()

    return render(request, 'view_patient.html', {'pat': pat})


def Add_Patient(request):

    if not request.user.is_staff:
        return redirect('login')

    error = ""

    if request.method == "POST":

        n = request.POST.get('name')
        g = request.POST.get('gender')
        m = request.POST.get('mobile')
        a = request.POST.get('address')

        try:
            Patient.objects.create(
                name=n,
                gender=g,
                mobile=m,
                address=a
            )

            error = "no"

        except Exception as e:
            print(e)
            error = "yes"

    return render(request, 'add_patient.html', {'error': error})


def Delete_Patient(request, pid):

    if not request.user.is_staff:
        return redirect('login')

    try:
        patient = Patient.objects.get(id=pid)
        patient.delete()

    except Patient.DoesNotExist:
        pass

    return redirect('view_patient')


# ================= APPOINTMENT =================

def View_Appointement(request):

    if not request.user.is_staff:
        return redirect('login')

    appoint = Appointment.objects.all()

    return render(request, 'view_appointement.html', {'appoint': appoint})


def Add_Appointment(request):

    if not request.user.is_staff:
        return redirect('login')

    doctor1 = Doctor.objects.all()
    patient2 = Patient.objects.all()

    error = ""

    if request.method == "POST":

        doctor_id = request.POST.get('doctor')
        patient_id = request.POST.get('patient')
        d1 = request.POST.get('date')
        t1 = request.POST.get('time')

        try:
            doctor = Doctor.objects.get(id=doctor_id)
            patient = Patient.objects.get(id=patient_id)

            Appointment.objects.create(
                doctor=doctor,
                patient=patient,
                date1=d1,
                Time1=t1
            )

            error = "no"

        except Exception as e:
            print(e)
            error = "yes"

    context = {
        'doctor': doctor1,
        'patient': patient2,
        'error': error
    }

    return render(request, 'add_appointment.html', context)


def Delete_Appointment(request, pid):

    if not request.user.is_staff:
        return redirect('login')

    try:
        appointment = Appointment.objects.get(id=pid)
        appointment.delete()

    except Appointment.DoesNotExist:
        pass

    return redirect('view_appointment')