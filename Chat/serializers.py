from rest_framework import serializers
from .models import *


class Custom_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Comment
		fields="__all__"


