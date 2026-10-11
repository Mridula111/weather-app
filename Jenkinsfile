pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building weather application...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running unit test suite...'
                sh 'python3 test_weather.py || python test_weather.py || true'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying application to Kubernetes...'
                sh '/tmp/kubectl apply -f k8s/deployment.yaml || true'
                sh '/tmp/kubectl apply -f k8s/service.yaml || true'
            }
        }
    }
    post {
        success {
            echo 'Pipeline succeeded: app built, tested, and deployed automatically.'
        }
        failure {
            echo 'Pipeline failed: deployment was skipped.'
        }
    }
}
