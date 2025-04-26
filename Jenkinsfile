pipeline {
    agent any

    environment {
        IMAGE_NAME = 'final_02-web'
        REPOSITORY = 'omhinge'
        TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📦 Checking out source code...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                script {
                    dockerImage = docker.build("${REPOSITORY}/${IMAGE_NAME}:${TAG}")
                }
            }
        }


    post {
        success {
            echo '✅ Deployment pipeline completed successfully!'
        }
        failure {
            echo '❌ Deployment pipeline failed. Check the logs.'
        }
    }
}
