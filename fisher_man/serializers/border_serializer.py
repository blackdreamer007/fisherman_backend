from rest_framework import serializers
from fisher_man.models.borders import Border

class BorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Border
        fields = ['id','border_name','latitude','longitude','created_at','is_active']
        read_only_fields = ['id', 'created_at']
