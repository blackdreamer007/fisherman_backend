from rest_framework import serializers
from fisher_man.models.fish_potentials import FishPotentials

class FishPotentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishPotentials
        fields = ['id','user','fish_name','quantity','latitude','longitude','created_at','is_active']
        read_only_fields = ['created_at']
