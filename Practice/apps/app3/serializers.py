from rest_framework import serializers
from apps.app3.models import Images  # Adjust the import based on your project structure

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id', 'name', 'file']  # Adjust fields as necessary

    def validate_image(self, value):
        # Custom validation logic for the image field
        if value.size > 5 * 1024 * 1024:  # 5MB limit
            raise serializers.ValidationError("Image file too large. Maximum size is 5MB.")
        if value.content_type not in ['image/jpeg', 'image/png', 'image/jpg']:
            raise serializers.ValidationError("Invalid file type. Only JPG, JPEG, and PNG are allowed.")
        return value