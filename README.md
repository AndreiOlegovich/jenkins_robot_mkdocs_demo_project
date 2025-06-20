# jenkins_robot_mkdocs_demo_project

## Precondition - SSH Keys

Need to generate SSH keys for Jenkins and MkDocs

Keys should be stored in ./keys/jenkins and ./keys/mkdocs directories

## Quick Start

Run

```
.\setup.ps1
```

or

```commandline
setup.sh
```

To start containers you can run

```commandline
docker compose up -d
```

To see the build logs run 

```commandline
docker compose build --progress=plain
```
instead. Or even

```commandline
docker compose build --no-cache --progress=plain  
```

## Jenkins

When Jenkins container is up and running visit

> http://localhost:8080/

And insert the password from installation logs to UI.

Logs can be found e.g in Docker Desktop *Logs* section of jenkins container.

