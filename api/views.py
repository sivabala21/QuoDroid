# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TestDataSerializer
import subprocess
import tempfile

class TestView(APIView):
    def post(self, request):
        serializer = TestDataSerializer(data=request.data)
        if serializer.is_valid():
            tests_data = serializer.validated_data['tests']
            with tempfile.NamedTemporaryFile(delete=False, suffix=".robot") as f:
                f.write(self.generate_robot_file(tests_data).encode('utf-8'))
                f_name = f.name
            process = subprocess.Popen(['robot', '-N', 'Test Case 1', f_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            return Response({'results': stdout.decode('utf-8')}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def generate_robot_file(self, tests_data):
        robot_file = f"""*** Settings ***
Library    SeleniumLibrary

*** Variables ***
"""
        for test_case in tests_data:
            for step in test_case['steps']:
                parts = re.split(r"((?:[\w']+)=)", step, maxsplit=1)
                if len(parts) == 3:
                    command, _, argument = parts
                    robot_file += f"${{arg{len(robot_file.splitlines())-1}}}     {argument.strip('\'')}\n"
                else:
                    command, argument = step.split(maxsplit=1)
                    robot_file += f"${{arg{len(robot_file.splitlines())-1}}}     {argument.strip('\'')}\n"
        robot_file += """*** Test Cases ***
Test Case 1"""
        for test_case in tests_data:
            robot_file += "\n    " + "    ".join(step.strip() for step in test_case['steps'])
        return robot_file

