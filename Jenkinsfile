pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --user pytest --break-system-packages --quiet || python3 -m pip install --user pytest --quiet'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 weather.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest test_weather.py -v'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh '/tmp/kubectl apply -f k8s/deployment.yaml'
                sh '/tmp/kubectl apply -f k8s/service.yaml'
                sh '/tmp/kubectl rollout status deployment/weather-app'
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
