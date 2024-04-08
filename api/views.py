# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TestDataSerializer
import subprocess
import re

def execute_robot_tests(test_data):
    # Extract commands and arguments from the steps
    commands = []
    arguments = []
    for test_case in test_data:
        for step in test_case['steps']:
            parts = re.split(r"((?:[\w']+)=)", step, maxsplit=1)
            if len(parts) == 3:
                command, _, argument = parts
                commands.append(command.strip())
                arguments.append(argument.strip())
            else:
                # Handle arguments without an equal sign
                command, argument = step.split(maxsplit=1)
                commands.append(command.strip())
                arguments.append(argument.strip())

    # Dynamically generate a .robot file with variables and test cases
    with open('dynamic_test.robot', 'w') as f:
        f.write("""*** Settings ***
Library    SeleniumLibrary

*** Variables ***
""")
        for i, argument in enumerate(arguments):
            if '=' in argument:
                arg_name, arg_value = argument.split('=', 1)
                f.write(f"${{arg_name}}     {arg_value}\n")
            else:
                arg_name = f"arg{i}"
                arg_value = argument
                f.write(f"${{arg_name}}     {arg_value}\n")

        f.write("""\n*** Test Cases ***
Test Case 1
""")
        for i, command in enumerate(commands):
            if arguments[i]:
                if '=' in arguments[i]:
                    arg_name = arguments[i].split('=', 1)[0]
                    f.write(f"    {command}     {arg_name}\n")
                else:
                    arg_name = f"arg{i}"
                    f.write(f"    {command}     ${{arg_name}}\n")
            else:
                f.write(f"    {command}\n")

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
