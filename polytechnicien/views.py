from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from .models import Member
from .forms import MemberForm, UserRegistrationForm
from django.contrib import messages
from rest_framework.views import APIView
from .serializers import MemberSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'polytechnicien/register.html', {'form': form})


def homepage(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Merci pour ton inscription!')
            return redirect('home')
    else:
        form = MemberForm()
    mens = Member.objects.all()
    return render(request, 'polytechnicien/index.html', {'form': form, 'mens': mens})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = AuthenticationForm()
    return render(request, 'polytechnicien/login.html', {'form': form})


def members(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    return render(request, 'polytechnicien/member_list.html', {'member': member})


def add(request):
    return render(request, 'polytechnicien/add.html')


def add_member(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        twitter = request.POST.get('twitter')
        linkedin = request.POST.get('linkedin')
        facebook = request.POST.get('facebook')
        website = request.POST.get('website')
        member = Member(full_name=full_name, email=email, twitter=twitter, linkedin=linkedin, facebook=facebook, website=website)
        member.save()
    return redirect('home')


def delete(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    return redirect('home')


def update(request, id):
    member = get_object_or_404(Member, id=id)
    return render(request, 'polytechnicien/update.html', {'member': member})


def update_member(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == "POST":
        member.full_name = request.POST.get('full_name')
        member.email = request.POST.get('email')
        member.twitter = request.POST.get('twitter')
        member.linkedin = request.POST.get('linkedin')
        member.facebook = request.POST.get('facebook')
        member.website = request.POST.get('website')
        member.save()
    return redirect('home')


class MemberView(APIView):
    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Data saved'}, safe=False)
        return JsonResponse({'message': 'Data not saved'}, safe=False)

    def get_student(self, id):
        return get_object_or_404(Member, id=id)

    def get(self, request, id=None):
        if id:
            member = self.get_student(id)
            serializer = MemberSerializer(member)
        else:
            members = Member.objects.all()
            serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    def put(self, request, id):
        member = get_object_or_404(Member, id=id)
        serializer = MemberSerializer(instance=member, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Data updated'}, safe=False)
        return JsonResponse({'message': 'Data not updated'}, safe=False)

    def delete(self, request, id):
        member = get_object_or_404(Member, id=id)
        member.delete()
        return JsonResponse({'message': 'Data deleted'}, safe=False)
