from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, Http404
from datetime import dt
from.models import PersonalInfo,Photo,Category,Location
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
