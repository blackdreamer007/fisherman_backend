from rest_framework import serializers
from fisher_man.models.emergency_requests import EmergencyRequests

class EmergencyRequestsSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    mobile = serializers.CharField(source='user.mobile', read_only=True)

    class Meta:
        model = EmergencyRequests
        fields = ['id','user', 'user_name', 'mobile', 'emergency_note','action_taken', 'latitude', 'longitude', 'created_at','is_active']
        read_only_fields = ['id', 'created_at']
