from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from fisher_man.models.fish_potentials import FishPotentials
from fisher_man.serializers.fish_potentials_serializer import FishPotentialsSerializer

class FishPotentialCreateUpdateView(APIView):
    def post(self, request):
        potential_id = request.data.get("id")

        if potential_id:
            # UPDATE
            try:
                instance = FishPotentials.objects.get(id=potential_id)
            except FishPotentials.DoesNotExist:
                return Response(
                    {"error": "Fish potential not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = FishPotentialsSerializer(
                instance,
                data=request.data,
                partial=True
            )

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Fish potential updated successfully"},
                    status=status.HTTP_200_OK
                )

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            # CREATE
            serializer = FishPotentialsSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Fish potential created successfully"},
                    status=status.HTTP_201_CREATED
                )

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FishPotentialsListView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        if user_id:
            logs = FishPotentials.objects.filter(user_id=user_id, is_active=True)
        else:
            logs = FishPotentials.objects.filter(is_active=True)
        serializer = FishPotentialsSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteFishPotentials(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        fish_id = request.data.get('id')

        if not user_id or not fish_id:
            return Response(
                {"error": "Both 'user_id' and 'id' are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            fish_potential = FishPotentials.objects.get(id=fish_id, user_id=user_id, is_active=True)
        except FishPotentials.DoesNotExist:
            return Response(
                {"error": "FishPotential not found or already inactive."},
                status=status.HTTP_404_NOT_FOUND
            )

        fish_potential.is_active = False
        fish_potential.save()

        return Response(
            {"success": f"FishPotential {fish_id} deactivated successfully."},
            status=status.HTTP_200_OK
        )