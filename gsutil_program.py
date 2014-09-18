gsutil -m cp gs://uspto-pair/applications/1210239*.zip gs://pairdata

sudo apt-get update
sudo apt-get install unzip

unzip  -jo  gs://pairdata/*.zip *-application_data.tsv -d gs://pairdata
rm gs://pairdata/*.zip
