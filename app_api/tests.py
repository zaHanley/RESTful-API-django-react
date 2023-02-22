from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Post, Category
from django.contrib.auth.models import User


class Post_Tests(APITestCase):

    def test_view_post(self):
        # reverse the endpoint
        #             app_name:url_name
        url = reverse('app_api:listcreate') 
        
        # simulate a browser making a get request to the url using JSON format
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

  
    def test_create_post(self):
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user(
            username='testuser1',
            password='123456789'
        )
        data = {
            "title": 'new',
            "author": 1,
            "excerpt": "new",
            "content": "new",
            }
        url = reverse('app_api:listcreate') 
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)