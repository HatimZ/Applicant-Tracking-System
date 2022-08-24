from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.preliminary_form.models import FormEntry
from apps.preliminary_form.rest_apis.serializers import UserSerializer


@api_view(['GET'])
def api_detail_user(request, slug):

    try:
        applicant = FormEntry.objects.get(email_address = slug)
    
    except FormEntry.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = UserSerializer(applicant)
        return Response(serializer.data)



