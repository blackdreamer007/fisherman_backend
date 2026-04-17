from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from fisher_man.serializers.emergency_requests_serializer import EmergencyRequestsSerializer
from fisher_man.models.emergency_requests import EmergencyRequests

class EmergencyRequestCreateView(APIView):
    def post(self, request):
        serializer = EmergencyRequestsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Emergency request created successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmergencyRequestListView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')

        if user_id:
            logs = EmergencyRequests.objects.filter(user_id=user_id)
        else:
            logs = EmergencyRequests.objects.all()

        serializer = EmergencyRequestsSerializer(logs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)