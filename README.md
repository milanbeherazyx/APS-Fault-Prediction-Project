**APS Fault Prediction Project**

This project aims to develop a fault prediction model for the Air Pressure System (APS) used in vehicles' braking systems. The goal is to detect potential APS faults early, which can lead to braking inefficiencies and compromise vehicle safety. By proactively identifying issues, we can minimize vehicle downtime, optimize performance, and reduce financial losses associated with delayed repairs.

**Problem Statement**
In vehicles, the air pressure system (APS) plays a critical role in the braking system's performance. APS faults can lead to braking inefficiencies and jeopardize vehicle safety. The current method of physically investigating APS failures is time-consuming and costly, causing financial losses and delays in repairing vehicles.

**Approach**
To address the problem, we utilized Python and implemented the XG Boost algorithm to achieve 97% accurate APS fault prediction. The project followed a comprehensive data analysis and modeling pipeline, which involved data collection, exploratory data analysis (EDA), preprocessing, and model selection. The solution was deployed using Docker containers with GitHub Actions for continuous deployment, leveraging AWS Elastic Container Registry (ECR) for secure container image storage.

To handle batch data processing and task scheduling, we integrated Apache Airflow into the project. This enabled us to automate report generation, schedule batch training for the model, and ensure timely execution of critical tasks. As a result, the analysis process was significantly faster, leading to cost-saving decisions.

**Use Case**
The APS fault prediction model provides substantial benefits to vehicle manufacturers and maintenance teams. By detecting potential APS issues early, it allows for proactive maintenance and timely repairs. The model's predictions also enable instant notifications to users, enhancing vehicle safety and optimizing braking system performance.

**Installation and Setup**
1. Clone this repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file using `pip install -r requirements.txt`.
3. Set up your environment variables by creating a `.env` file and providing necessary configurations.

**Usage**
1. Run the main script `python main.py` to execute the APS fault prediction model.
2. Use the provided APIs for data retrieval and model predictions.
3. Check the generated reports and visualizations to monitor the model's performance.

**Contributing**
We welcome contributions to this project. Please fork the repository, make your changes, and submit a pull request.

**License**
This project is licensed under the MIT License - see the `LICENSE` file for details.

**Contact**
For any inquiries or feedback, please contact [your-email@example.com](mailto:your-email@example.com).

(Note: Replace `[your-email@example.com](mailto:your-email@example.com)` with your actual contact email address.)


for linux:
$(pwd)/airflow/dags

for windows"
%cd%\airflow\dags

docker run -p 8080:8080 -v "/home/milanbeherazyx/Data Science/sensor_fault_detection/airflow/dags:/app/airflow/dags" sensor:latest

docker run -p 8080:8080 -v "/home/milanbeherazyx/Data Science/sensor_fault_detection/airflow/dags:/app/airflow/dags" -e "mongodb+srv://milanbeherazyx:zSR1HZte2oPjMeKe@cluster0.wui6u7y.mongodb.net/?retryWrites=true&w=majority" sensor:latest 


docker run -p 8080:8080 -v $(pwd)/airflow/dags:/app/airflow/dags -e "mongodb+srv://milanbeherazyx:zSR1HZte2oPjMeKe@cluster0.wui6u7y.mongodb.net/?retryWrites=true&w=majority" sensor:latest 



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
