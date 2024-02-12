cp .\keys\jenkins\*rsa* .\dockerfiles\jenkins\.ssh
cp .\keys\mkdocs\id_rsa* .\dockerfiles\mkdocs\.ssh

docker compose up --detach --build jenkins

rm .\dockerfiles\jenkins\.ssh\*rsa*
rm .\dockerfiles\mkdocs\.ssh\id_rsa*