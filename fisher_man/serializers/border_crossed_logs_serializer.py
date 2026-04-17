from rest_framework import serializers
from fisher_man.models.border_crossed_logs import BorderCrossedLogs

class BorderCrossedLogsSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    mobile = serializers.CharField(source='user.mobile', read_only=True)

    class Meta:
        model = BorderCrossedLogs
        fields = [
            'id',
            'user',
            'user_name',
            'mobile',
            'latitude',
            'longitude',
            'note',
            'created_at',
            'is_active'
        ]
