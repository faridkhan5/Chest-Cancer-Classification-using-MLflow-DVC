# Chest-Cancer-Classification-using-MLflow-DVC

## About
This project leverages the VGG-16 CNN model to classify chest cancer from medical imaging data. It is built around a modular pipeline that leverages tools like MLflow, DVC, Docker, and GitHub Actions. Deployment is managed on AWS EC2 via Docker images stored in Amazon ECR.

## Features
* Modular pipeline structure for scalability and maintainability.
* Pretrained VGG-16 model is fine-tuned using TensorFlow to achieve an accuracy of 84%
* Experiment tracking with MLflow, integrated with Dagshub for performance monitoring.
* Data and model versioning using DVC.
* Containerized deployment using Docker, hosted on AWS EC2.
* Automated CI/CD pipeline setup with GitHub Actions.

## Tech Stack
* **TensorFlow:** Training the VGG-16 model
* **MLflow:** Experiment tracking and logging model performance metrics
* **Dagshub:** Platform for integrating MLflow to visualize and collaborate on tracked experiments
* **DVC:** Version control for datasets, models, and pipeline stages to ensure reproducibility
* **Docker:** Containerization of the application for consistent deployment across environments
* **Amazon ECR:** Repository for storing Docker images
* **AWS EC2:** Cloud service for deploying the application
* **GitHub Actions:** Automation of CI/CD pipeline, including testing, building, and deployment

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml


### Dagshub

MLFLOW_TRACKING_URI=https://dagshub.com/faridkhan5/Chest-Cancer-Classification-using-MLflow-DVC.mlflow \
MLFLOW_TRACKING_USERNAME=faridkhan5 \
MLFLOW_TRACKING_PASSWORD= \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/faridkhan5/Chest-Cancer-Classification-using-MLflow-DVC.mlflow

export MLFLOW_TRACKING_USERNAME=faridkhan5

export MLFLOW_TRACKING_PASSWORD=

```

 ### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 556589063388.dkr.ecr.eu-north-1.amazonaws.com/kidney

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
## 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


## 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = 

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = kidney
