
from rest_framework import serializers

from apps.preliminary_form.models import FormEntry



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormEntry
        fields = ['first_name', 'last_name' , 'email_address' , 'experience' , 'visa_status']





