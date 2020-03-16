
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
> cd e2e_template  

**To run tests from the local environment**  

Using below command you can check all environments like: production, local instances etc.  
You only need to know domain, username, password and tag(s) and insert them into belows command.  

> bin/run.sh -d {domain} -u {user} -p {password} tests-local --tags=canartest
