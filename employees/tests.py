# employees/tests.py
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from .models import Employee
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class EmployeeAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        
        # Create an employee
        self.employee = Employee.objects.create(name="John Doe", email="john@example.com", department="HR", role="Manager")

    def test_create_employee(self):
        url = reverse('employee-list-create')
        data = {"name": "Jane Doe", "email": "jane@example.com", "department": "Engineering", "role": "Developer"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_employees(self):
        url = reverse('employee-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)  # Check for pagination

    def test_retrieve_employee(self):
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employee(self):
        url = reverse('employee-detail', args=[self.employee.id])
        data = {
            "name": "John Doe Updated",
            "email": "john.updated12@example.com",  # Use a unique email for the update
            "department": self.employee.department,
            "role": self.employee.role,
        }
        response = self.client.put(url, data, format='json')
        
        # Print response data for debugging
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "John Doe Updated")



    def test_delete_employee(self):
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
