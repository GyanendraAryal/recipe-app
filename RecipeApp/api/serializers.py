from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from .models import *


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    bio = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField()
    phone = PhoneNumberField(("Phone Number"), blank=True, region="NP")
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


class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    user_name = serializers.CharField(source="user.name", read_only=True)
    title = serializers.CharField(max_length=100)
    ingrediants = serializers.CharField(style={"base_template": "textarea.html"})
    cooking_duration = serializers.DurationField()
    dificulty = serializers.ChoiceField(
        choices=[("EA", "Easy"), ("MD", "Medium"), ("HD", "Hard")], default="EA"
    )
    # comment
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        user_id = validated_data.pop("user_id")
        return Recipe.objects.create(user_id=user_id, **validated_data)

    def update(self, instance, validated_data):
        if "user_id" in validated_data:
            instance.user_id = validated_data.get("user_id")
        instance.title = validated_data.get("title", instance.title)
        instance.ingrediants = validated_data.get("ingrediants", instance.ingrediants)
        instance.cooking_duration = validated_data.get(
            "cooking_duration", instance.cooking_duration
        )
        instance.dificulty = validated_data.get("dificulty", instance.dificulty)
        instance.save()
        return instance
