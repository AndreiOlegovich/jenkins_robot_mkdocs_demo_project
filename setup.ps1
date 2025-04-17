#!\bin\bash
# Download dos2unix app for Windows https://sourceforge.net/projects/dos2unix/
# Or comment out dos2unix lines and convert files elsewhere

dos2unix dockerfiles/mkdocs/entrypoint.sh
dos2unix dockerfiles/robot/entrypoint.sh

cp .\keys\jenkins\*rsa* .\dockerfiles\jenkins\.ssh
cp .\keys\mkdocs\id_rsa* .\dockerfiles\mkdocs\.ssh

docker compose build
docker compose up -d

rm .\dockerfiles\jenkins\.ssh\*rsa*
rm .\dockerfiles\mkdocs\.ssh\id_rsa*
