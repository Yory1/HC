from django.shortcuts import render, get_object_or_404
from main.utils import get_object_or_none
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group



def Doctor_Details(request,NN):

    doctor = get_object_or_404(Physician, physician_nn=NN)
    #handle clinicworkingtime
    physicianclinicworkingtime = PhysicianClinicWorkingTime.objects.filter(physician_nn=NN)
    for clinic in physicianclinicworkingtime[1:] :
        first_clinic=clinic.clinic
    clinic_id = first_clinic.clinic
    clinic =get_object_or_404(Clinic, clinic=clinic_id)
    #handle hospitalworkingtime
    physicianhospitalworkingtime = PhysicianHospitalWorkingTime.objects.filter(physician_nn=NN)
    for hospital in physicianhospitalworkingtime[1:] :
    	first_hospital=hospital.hospital
    hospital_id = first_hospital.hospital
    hospital = get_object_or_404(Hospital, hospital=hospital_id)

    stakeholder = get_object_or_404(Stakeholders, national_number=NN)
    #handle rating
    physicianrating = None
    physicianratingcount = "no"
    if PhysicianRating.objects.filter(physician_nn=NN):
    	physicianrating = PhysicianRating.objects.filter(physician_nn=NN)
    	physicianratingcount =PhysicianRating.objects.filter(physician_nn=NN).count()
    #handle user as patient
    patient = request.user
    stakeholder_user = get_object_or_404(Stakeholders, national_number=patient)
    patient_nn = get_object_or_404(Patient, patient_nn=stakeholder_user)
    
    context = {
        "doctor": doctor,
        'stakeholder': stakeholder,
        'physicianclinicworkingtime':physicianclinicworkingtime,
        'physicianhospitalworkingtime':physicianhospitalworkingtime,
        'clinic':clinic,
        'hospital':hospital,
        'physicianrating':physicianrating,
        'physicianratingcount':physicianratingcount,
        'stakeholder_user':stakeholder_user,
        
    }
    
    if request.method == 'POST':

    	# if review ---------------------------------------

	    current_rate =request.POST.get('rate')
	    comment = request.POST.get('patient_comment')
	    if patient_nn :
	    	rate = PhysicianRating.objects.filter(patient_nn=patient_nn).update(rate=current_rate)	
	    if current_rate : 
	    	user_rating = PhysicianRating.objects.create(
		        	patient_nn=patient_nn,
		    		physician_nn = doctor,
		    		patient_comment = comment,
		   			rate = current_rate,
	    			)
	    		    
	    	return HttpResponse()
	    # if booking ---------------------------------------	
	    if 'booking_button' in request.POST:

	    	message = request.POST.get('message'),
	    	if message:
	    		booking = PhysicianPatientBooking.objects.create(
			    	patient_nn = patient_nn,
				    physician_nn =doctor,
				    booking_date_clinic = "2020-02-25",
				    booking_date_hospital = "2020-02-25",
				    clinic = clinic,
				    hospital = hospital,
				    phone = request.POST.get('phone'),
				    email = request.POST.get('email'),
				    message = message,
		    	)

	    	return HttpResponse()

    return render(request, 'vezeeta/doctor/Doctor_Details.html',context)





def Clinic_Details(request,id):

    clinic =get_object_or_404(Clinic, clinic=id)
    medicalinstitution = get_object_or_404(MedicalInstitutions, institution_id=id)
    #handle rating
    clinicrating= None 
    clinicratingcount = "No"
    if ClinicRating.objects.filter(clinic=id):
   		clinicrating = ClinicRating.objects.filter(clinic=id)
   		clinicratingcount = ClinicRating.objects.filter(clinic=id).count()
   	#handle user as patient	
    patient = request.user
    stakeholder_user = get_object_or_404(Stakeholders, national_number=patient)
    patient_nn = get_object_or_404(Patient, patient_nn=stakeholder_user)
    #handle clinicworkingtime
    physicianclinicworkingtime = PhysicianClinicWorkingTime.objects.filter(clinic=id)
    specialization_list = []
    for doctor in physicianclinicworkingtime :
    	stakeholder = get_object_or_404(Stakeholders, national_number=doctor)
    	doctor = get_object_or_404(Physician, physician_nn=stakeholder)
    	specialization_list.append(PhysicianSpecialization.objects.filter(physician_nn=doctor))
 
    context = {
        'clinic':clinic,
        'medicalinstitution':medicalinstitution,
        'clinicrating':clinicrating,
        'clinicratingcount':clinicratingcount,
        'stakeholder_user':stakeholder_user,
        'physicianclinicworkingtime':physicianclinicworkingtime,
        'specialization_list':specialization_list	,
        
    }
    
    if request.method == 'POST':

    	# if review ---------------------------------------


	    current_rate =request.POST.get('rate')
	    comment = request.POST.get('patient_comment')
	    if patient_nn :
	    	rate = ClinicRating.objects.filter(patient_nn=patient_nn).update(rate=current_rate)	
	    if current_rate : 
	    	user_rating = ClinicRating.objects.create(
		        	patient_nn=patient_nn,
		    		clinic = clinic,
		    		patient_comment = comment,
		   			rate = current_rate,
	    			)
	    		    
	    	return HttpResponse()
	    # if booking ---------------------------------------	
	    if 'booking_button' in request.POST:
	    	selected_doctor = request.POST.get('physician_nn'),
	    	print(selected_doctor)
	    	selected_doctor_instance = get_object_or_404(Physician, physician_nn=selected_doctor)
	    	message = request.POST.get('message'),
	    	if message:
	    		booking = ClinicPatientBooking.objects.create(
			    	patient_nn = patient_nn,
				    physician_nn =selected_doctor_instance,
				    booking_date_clinic = "2020-02-25",
				    clinic = clinic,
				    phone = request.POST.get('phone'),
				    email = request.POST.get('email'),
				    message = message,
		    	)

	    	return HttpResponse()

    return render(request, 'vezeeta/clinic/Clinic_Details.html',context)