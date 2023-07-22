# sensor_fault_detection
This is a fault detection project using sensor reading.


for linux:
$(pwd)/airflow/dags

docker run -p 8080:8080 -v %cd%\airflow\dags:/app/airflow/dags -e 'MONGO_DB_URL=mongodb+srv://avnish:Aa327030@cluster0.or68e.mongodb.net/?retryWrites=true&w=majority' sensor:latest 



Github Secrets:
```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
AWS_ECR_LOGIN_URI=
ECR_REPOSITORY_NAME=
BUCKET_NAME=
MONGO_DB_URL=
```