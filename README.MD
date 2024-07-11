# Dynamic Test Execution with Django and Robot Framework

## Introduction

This document outlines a method for dynamically generating and executing test cases using Django, a high-level Python web framework, and Robot Framework, a generic test automation framework.

## Problem Statement

In automated testing scenarios, there might be a need to execute test cases with dynamic parameters. Handling such dynamic inputs efficiently and executing tests seamlessly becomes a challenge. This document presents a solution to this problem using Django and Robot Framework.

## Solution Overview

The solution involves creating a Django API endpoint that receives test data, dynamically generates Robot Framework test cases based on the input, executes these tests, and returns the results. Key components of the solution include:

- Django: Provides the web framework for building the API endpoint.
- Robot Framework: Enables test case generation and execution.
- SeleniumLibrary: A Robot Framework library for automating web browsers.

## Implementation Details

### Django Setup

1. **Installation**: Install Django using pip:

2. **Project Initialization**: Create a Django project using the `django-admin` command:

3. **App Creation**: Create a Django app for handling test execution:

4. **URL Configuration**: Define URL patterns in the `urls.py` file.

### Robot Framework Setup

1. **Installation**: Install Robot Framework and SeleniumLibrary using pip:

2. **Test Data Serializer**: Define a serializer for handling incoming test data.

3. **Test Execution Function**: Implement a function (`execute_robot_tests`) to dynamically generate and execute Robot Framework test cases.

4. **Django View**: Create a Django APIView (`TestView`) to handle POST requests containing test data.

5. **URL Routing**: Configure a URL route to map requests to the `TestView`.

### Test Case Generation

1. **Extract Commands and Arguments**: Parse test steps to extract commands and arguments.

2. **Dynamically Generate Test Cases**: Generate a `.robot` file dynamically with variables and test cases based on extracted data.

3. **Execute Test Suite**: Execute the dynamically generated test suite using the `subprocess` module.

## Usage

1. Start the Django development server:

2. Send a POST request to the specified endpoint (`/tests/api`) with test data formatted according to the `TestDataSerializer`.

3. Receive test execution results in the response.

## Usage

1. **Send a POST Request:**

   - Construct a POST request to the specified endpoint (e.g., `http://127.0.0.1:8000/tests/api`).
   - Include test data in the request body formatted according to the `TestDataSerializer`.

2. **Receive Test Results:**
   The response will contain the test execution results (success/failure and details).

## Example Usage (assuming TestDataSerializer expects a list of dictionaries, each with a 'steps' key):

```json
{
  "tests": [
    {
      "title": "Login with correct Username and Password",
      "steps": [
        "Open Browser url='https://the-internet.herokuapp.com/login'",
        "Input Text          username username='tomsmith'",
        "Input Text          password password='SuperSecretPassword!'",
        "Click Element     button=xpath:/html/body/div[2]/div/div/form/button/i"
      ]
    }
  ]
}
```
## Video Demo:

![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTJzNGl3djNoNWk4djBsMXhxd3FvNXQ3bXhueXc3cWozd2hmdjZmMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NvD18VslmsFaPNKPVY/giphy.gif)


## Conclusion

By leveraging Django and Robot Framework, it's possible to dynamically generate and execute test cases with varying parameters efficiently. This solution provides a flexible and scalable approach to automated testing, enabling seamless integration into continuous integration and deployment pipelines.

For detailed code implementation, refer to the provided code snippets and integrate them into your Django project.

---

This document provides an overview of a solution for dynamic test execution using Django and Robot Framework. For detailed implementation steps and code snippets, please refer to the accompanying code repository.
