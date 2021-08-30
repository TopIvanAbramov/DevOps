pipeline {
    agent {
        docker {
            image 'python:3.9-alpine3.14'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r app_python/requirements.test.txt -r app_python/requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
    }
}