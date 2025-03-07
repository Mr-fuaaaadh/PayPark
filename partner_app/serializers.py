from rest_framework import serializers
from .models import *

class ParkOwnerSerializers(serializers.ModelSerializer):
    class Meta :
        model = PlotOnwners
        fields = "__all__"

class VehicleManagementSerializer(serializers.ModelSerializer):
    class Meta :
        model = Vehicle
        fields = "__all__"

                   

class ParkingStationImages(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"

    
    
class VehiclePricingManagementSerializer(serializers.ModelSerializer):
    class Meta :
        model = ParkingCharge
        fields = "__all__"

class ParkingPlotsSerializrs(serializers.ModelSerializer):
    class Meta :
        model = ParkingPlots
        fields = "__all__"



        
class AdminAllParkingPlosView(serializers.ModelSerializer):
    class Meta :
        model = ParkingPlots
        fields = "__all__"
        
class PaymentModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ParkingReservationPayment
        fields = "__all__"
        
class ParkingReservatonSerializers(serializers.ModelSerializer):
    reservations = PaymentModelSerializers(read_only=True, many=True)
    class Meta :
        model = ParkingReservationPayment
        fields = "__all__"     
        
class ParkOwnerAllDatasFetching(serializers.ModelSerializer):
    images = ParkingStationImages(many=True, read_only=True)
    pricing = VehiclePricingManagementSerializer(read_only=True, many=True)
    plots = ParkingPlotsSerializrs(read_only=True, many=True)
    payments = serializers.SerializerMethodField()


    class Meta:
        model = PlotOnwners
        fields = [
            'id',
            'ownerID',
            'owner_name',
            'owner_email',
            'owner_phone',
            'owner_address',
            'latitude',
            'longitude',
            'account_number',
            'ifsc_code',
            'ownership_type',
            'created_at',
            'images',
            'pricing',
            'plots',
            # 'reservations',
            'payments'
        ]

    def get_payments(self,obj):
        payment  = ParkingReservationPayment.objects.filter(plot = obj.id)
        serializer = PaymentModelSerializers(payment, many=True)
        return serializer.data
        

