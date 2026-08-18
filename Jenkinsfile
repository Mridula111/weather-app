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
                sh 'pip install pytest --break-system-packages --quiet || pip install pytest --quiet'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 weather.py'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest test_weather.py -v'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
                sh 'kubectl rollout status deployment/weather-app'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'weather.py', fingerprint: true, allowEmptyArchive: true
        }
    }
}