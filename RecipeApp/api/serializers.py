from rest_framework import serializers
from .models import *


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    bio = serializers.CharField(required=False, blank=True)
    email = serializers.EmailField(unique=True)
    phone = serializers.PhoneNumberField(_("Phone Number"), blank=True, region="NP")
    profile_image = serializers.ImageField(required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        full_name = f"{validated_data.get('first_name','')} {validated_data.get('last_name', '')}".strip()
        return User.objects.create(
            name=full_name,
            bio=validated_data.get("bio", ""),
            email=validated_data.get("email"),
            phone=validated_data.get("phone", ""),
            profile_image=validated_data.get("profile_image"),
        )

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.bio = validated_data.get("bio", instance.bio)
        instance.email = validated_data.get("email", instance.email)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.profile_image = validated_data.get(
            "profile_image", instance.profile_image
        )
        instance.save()
        return instance
