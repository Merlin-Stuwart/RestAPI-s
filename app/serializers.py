from rest_framework import serializers
from app.models import *

class productMs(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'