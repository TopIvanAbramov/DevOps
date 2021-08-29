[![Docker CI Actions Status](https://github.com/topivanabramov/devops/workflows/docker-ci/badge.svg)](https://github.com/topivanabramov/devops/actions) 

## **Containerized web application**

> Ivan Abramov
> BS-18 SE-1


#### Project description

App shows current time in Moscow on localhost with port 5000

Docker image is available [here](https://hub.docker.com/repository/docker/ivanabramov/devops)

#### Installation

1) Clone repository
2) Build and run docker image

```
docker build -t flask_app . 
docker run --rm -p 5000:5000 flask_app
```

 To view app visit: http://localhost:5000

#### Used linters for code optimization

- [hadolint](https://github.com/hadolint/hadolint) 
- [Pylint](https://www.pylint.org)
- [MarkdownLint](https://github.com/DavidAnson/markdownlint)

#### Run unit tests

```
pytest
```

