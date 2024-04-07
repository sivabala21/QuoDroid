# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TestDataSerializer
import subprocess

import subprocess

def execute_robot_tests(test_data):
    # Dynamically generate a .robot file with test data
    # For simplicity, let's assume test_data is a list of dictionaries with 'title' and 'steps'
    with open('dynamic_test.robot', 'w') as f:
        for test_case in test_data:
            title = test_case['title']
            steps = '\n'.join([f"    {step}" for step in test_case['steps']])
            f.write(f"""
*** Test Cases ***
{title}
{steps}
""")

    # Execute the dynamically generated test suite
    result = subprocess.run(['robot', 'dynamic_test.robot'], capture_output=True)

    # Return the test execution result
    return result.stdout.decode('utf-8')


class TestView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TestDataSerializer(data=request.data)
        if serializer.is_valid():
            tests_data = serializer.validated_data['tests']
            test_results = execute_robot_tests(tests_data)
            return Response({'results': test_results}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



