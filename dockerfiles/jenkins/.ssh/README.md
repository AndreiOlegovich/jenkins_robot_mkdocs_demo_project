ssh keys will be moved here from original keys/ dir

Currently there is still minor misconfig in Dockerfile so after first start need to run several commands inside Jenkins container

```
bash
su jenkins
cp /home/jenkins/.ssh/config /var/jenkins_home/.ssh/config
cp /home/jenkins/.ssh/jenkins_rsa* /var/jenkins_home/.ssh/
chmod 400 /var/jenkins_home/.ssh/jenkins_rsa
```

then you can run

```
ssh mkdocs.andrei.com
ssh jenkins@mkdocs.andrei.com
```

