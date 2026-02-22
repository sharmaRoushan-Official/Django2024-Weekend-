from rest_framework import serializers
from EMS.models import Employee
from demoApi.models import Trainer
from EMS.models import Employee


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


# serializers.ModelSerializer is a shortcut that automatically creates a serializer class based on the model fields.

# Meta class is used to specify the model and fields to be included in the serialization.
# model = Trainer indicates that this serializer is for the Trainer model.
# fields = '__all__' means that all fields of the Trainer model should be included in the serialization.