from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile

class ImageUploadTests(APITestCase):
    def test_upload_image_success(self):
        url = reverse('upload-image')  # Adjust the URL name as per your urls.py
        with open('path/to/test/image.jpg', 'rb') as image_file:  # Use a valid test image path
            response = self.client.post(url, {'image': image_file}, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('file_path', response.data)

    def test_upload_image_no_file(self):
        url = reverse('upload-image')  # Adjust the URL name as per your urls.py
        response = self.client.post(url, {}, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'No file provided'})

    def test_upload_image_invalid_type(self):
        url = reverse('upload-image')  # Adjust the URL name as per your urls.py
        invalid_file = SimpleUploadedFile("test.txt", b"file_content", content_type="text/plain")
        response = self.client.post(url, {'image': invalid_file}, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'Invalid file type'})