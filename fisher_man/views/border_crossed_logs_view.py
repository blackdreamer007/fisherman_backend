from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from fisher_man.serializers.border_crossed_logs_serializer import BorderCrossedLogsSerializer
from fisher_man.models.border_crossed_logs import BorderCrossedLogs


class CreateBorderCrossedLogView(APIView):
    def post(self, request):
        serializer = BorderCrossedLogsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Border crossed log created successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BorderCrossedLogsListView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')

        logs = BorderCrossedLogs.objects.select_related('user')

        if user_id:
            logs = logs.filter(user_id=user_id)

        serializer = BorderCrossedLogsSerializer(logs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

