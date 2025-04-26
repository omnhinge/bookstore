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
                echo '🐳 Building Docker image locally...'
                script {
                    docker.build("${REPOSITORY}/${IMAGE_NAME}:${TAG}")
                }
            }
        }
    }

    post {
        success {
            echo '✅ Build completed locally!'
        }
        failure {
            echo '❌ Build failed.'
        }
    }
}
