## QA - e2e test template 

This template configure selenium, behave and pytest that are required to create test scenarios.
There is an example of test for pytest, as well as for selenium using page object pattern. 

## Installation requirements

Install docker - https://www.docker.com/get-started 

Allow your user to run docker (linux only):  
>sudo usermod -G docker -a $USER  

## **Usage:**

> bin/run.sh tests

If the test pass (green) it means that the test environment is ready.

**To run tests from the local environment**  
You can write tests either in behave or pytest - choose your framework and comment out the one you won't use
in [docker/start-app.sh](docker/start-app.sh) (line 23,24)

**BEHAVE**:

Directory structure:
> tests/features/lib/pages -> page object definition

> tests/features/lib/pages/__init__.py -> if you want to add a new page object definition file, you must also add it to this file

> tests/features/steps -> steps definition

> tests/features/ -> tests files

If you want to run tests:

> bin/run.sh tests --tags=your_tags

**PYTEST**:

Directory structure:
tests/ -> tests files

If you want to run tests:

> bin/run.sh tests -m your_tags
