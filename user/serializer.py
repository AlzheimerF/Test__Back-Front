from rest_framework import serializers
from user.models import InfoUser, Profession
from django.contrib.auth.models import User

class ProfessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profession
        fields = ['title', 'description', 'prof_id']

    def create(self, validated_data):
        profession = Profession.objects.create(
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            prof_id=validated_data.get('prof_id'),
        )
        return profession

class InfoUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfoUser
        fields = ['country', 'language', 'gender', 'about_yourself', 'info_id']

    def create(self, validated_data):
        infouser = InfoUser.objects.create(
            country=validated_data.get('country'),
            language=validated_data.get('language'),
            gender=validated_data.get('gender'),
            about_yourself=validated_data.get('about_yourself'),
            info_id=validated_data.get('info_id'),
        )
        return infouser

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'last_name',
            'email',
            'password',
        )

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data.get('username'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            )
        return user


