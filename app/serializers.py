from rest_framework import serializers
from datetime import date
from .models import Fashion
from .ai import predict_fashion

"""
FashionTestSerializer : personal color test input 검증 및 db 저장
"""

class FashionTestSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Fashion
        fields = ['color', 'image']

    def ai_model(self, color, file):  # 아직 ai model 연결되지 않음
        return predict_fashion(color, file)

    def create(self, validated_data):
        res = self.ai_model(validated_data['color'], validated_data['image'])
        return Fashion.objects.create(**validated_data, date=date.today(), **res)