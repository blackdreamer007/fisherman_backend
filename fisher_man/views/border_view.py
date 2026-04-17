from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from fisher_man.models.borders import Border
from fisher_man.serializers.border_serializer import BorderSerializer


class CreateEditBorderView(APIView):
    def post(self, request):
        border_id = request.data.get("id")
        if border_id:
            try:
                border = Border.objects.get(id=border_id)
            except Border.DoesNotExist:
                return Response(
                    {"error": "Border not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = BorderSerializer(border, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Border updated successfully"},
                    status=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            serializer = BorderSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Border created successfully"},
                    status=status.HTTP_201_CREATED
                )

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BorderActiveUpdateView(APIView):
    def patch(self, request, border_id):
        try:
            border = Border.objects.get(id=border_id)
        except Border.DoesNotExist:
            return Response(
                {"error": "Border not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        is_active = request.data.get("is_active")

        if is_active is None:
            return Response(
                {"error": "is_active field is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        border.is_active = is_active
        border.save(update_fields=["is_active"])

        return Response(
            {
                "message": "Border status updated successfully",
                "border_id": border.id,
                "is_active": border.is_active
            },
            status=status.HTTP_200_OK
        )

class BorderListView(APIView):
    def get(self, request):
        borders = Border.objects.filter(is_active=True)
        serializer = BorderSerializer(borders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)