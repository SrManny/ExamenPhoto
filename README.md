# Exam Photoslurp

## Installation

First create the docker image using the command of build.txt

```bash
docker build -t photoslurpexam --rm .
```

Then create the docker conteiner using the command of launcher.txt. 

```bash
docker run -d --name photoslurpExam_cont -p 0.0.0.0:5000:5000 photoslurpexam
```


To check if the docker is really running, you can use:

```bash
docker logs photoslurpExam_cont 
```
or
```bash
docker ps -a
```

## Test
There are some features tested in the file test.py. In order to test the app just change the host to the host on is running the docker.
