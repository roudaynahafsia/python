from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ("full_name", "email", "twitter", "linkedin", "facebook", "website")