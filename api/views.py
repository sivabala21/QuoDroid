# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TestDataSerializer

class TestView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TestDataSerializer(data=request.data)
        if serializer.is_valid():
            # Process the data here
            tests_data = serializer.validated_data['tests']
            for test_data in tests_data:
                title = test_data['title']
                steps = test_data['steps']
            print(title,steps)
                # Process each step and title as needed
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
