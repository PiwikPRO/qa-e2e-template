
# **Usage:**  

**Step by step**  

For the beginning, please install:  
* docker-engine 17.03 or newer -> https://docs.docker.com/install/linux/docker-ce/debian/  
* docker-compose 1.12.0 or newer -> https://docs.docker.com/compose/install/  

Allow your user to run docker:  

>usermod -G docker -a $USER  

Next, please clone the repository  
> git clone git@github.com:PiwikPRO/e2e_template.git
>  
> cd PPMS-e2e_template


> bin/run.sh tests

If the test pass (green) it means that the test environment is ready.

**To run tests from the local environment**  
Choose your framework:

In file
docker/start-app.sh
comment a framework you won't use (line 22,23)

BEHAVE:

Directory structure:
> tests/features/lib/pages -> page object definition

> tests/features/lib/pages/__init__.py -> if you want to add a new page object definition file, you must also add it to this file

> tests/features/steps -> steps definition

> tests/features/ -> tests files

If you want to run tests:

> bin/run.sh tests --tags=your_tags

PYTEST:

Directory structure:
tests/ -> tests files

If you want to run tests:

> bin/run.sh tests -m your_tags
