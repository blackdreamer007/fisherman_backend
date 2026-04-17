from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from fisher_man.models.borders import Border
from fisher_man.models.border_crossed_logs import BorderCrossedLogs
from fisher_man.models.fish_potentials import FishPotentials
from fisher_man.models.emergency_requests import EmergencyRequests
from fisher_man.models.user import User
from fisher_man.models.dashboard_count import DashboardCount


class DashboardCountView(APIView):
    def get(self, request):
        borders_count = Border.objects.filter(is_active=True).count()
        border_crossed_count = BorderCrossedLogs.objects.filter(is_active=True).count()
        fishing_zones_count = FishPotentials.objects.filter(is_active=True).count()
        emergencies_count = EmergencyRequests.objects.filter(is_active=True).count()
        fishermans_count = User.objects.filter(
            user_type='Fisherman',
            is_active=True
        ).count()

        data = {
            "borders": borders_count,
            "border_crossed": border_crossed_count,
            "fishing_zones": fishing_zones_count,
            "emergencies": emergencies_count,
            "fishermans": fishermans_count
        }

        # SAVE OR UPDATE SINGLE ROW
        obj, created = DashboardCount.objects.get_or_create(id=1)

        obj.borders = borders_count
        obj.border_crossed = border_crossed_count
        obj.fishing_zones = fishing_zones_count
        obj.emergencies = emergencies_count
        obj.fishermans = fishermans_count
        obj.save()

        return Response(data, status=status.HTTP_200_OK)

class UserDashboardCountView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")

        if not user_id:
            return Response(
                {"error": "user_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(id=user_id, user_type='Fisherman')
        except User.DoesNotExist:
            return Response(
                {"error": "Fisherman not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        borders_count = Border.objects.filter(is_active=True).count()

        border_crossed_count = BorderCrossedLogs.objects.filter(
            user=user,
            is_active=True
        ).count()

        fishing_zones_count = FishPotentials.objects.filter(
            user=user,
            is_active=True
        ).count()

        emergencies_count = EmergencyRequests.objects.filter(
            user=user,
            is_active=True
        ).count()

        data = {
            "borders": borders_count,
            "border_crossed": border_crossed_count,
            "fishing_zones": fishing_zones_count,
            "emergencies": emergencies_count
        }

        return Response(data, status=status.HTTP_200_OK)