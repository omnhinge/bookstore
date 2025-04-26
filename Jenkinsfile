pipeline {
    agent any

    environment {
        // Docker settings
        DOCKER_IMAGE = 'final_02-web' 
        DOCKER_TAG = 'latest'
        DOCKER_REGISTRY = 'docker.io'  
        REPOSITORY = 'omhinge'
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub
                git 'https://github.com/omnhinge/bookstore.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image based on your Dockerfile
                    echo 'Building Docker image...'
                    sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
                }
            }
        }

        stage('Run Migrations & Tests') {
            steps {
                script {
                    // Run migrations inside the container (Django-specific)
                    echo 'Running migrations...'
                    sh 'docker-compose -f $DOCKER_COMPOSE_FILE run --rm web python manage.py migrate'
                    
                    // Run tests (if any, modify to your testing setup)
                    echo 'Running tests...'
                    sh 'docker-compose -f $DOCKER_COMPOSE_FILE run --rm web python manage.py test'
                }
            }
        }

        stage('Push Docker Image to Registry') {
            when {
                branch 'main'  // Run this stage only on the 'main' branch or change as necessary
            }
            steps {
                script {
                    echo 'Pushing Docker image to registry...'
                    sh 'docker push $DOCKER_IMAGE:$DOCKER_TAG'
                }
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'  // Run this stage only on the 'main' branch or change as necessary
            }
            steps {
                script {
                    // Deploy to production (customize your deployment as needed)
                    echo 'Deploying to production...'
                    sh 'ssh your_server_user@your_server_ip "docker-compose -f $DOCKER_COMPOSE_FILE down && docker-compose -f $DOCKER_COMPOSE_FILE up -d"'
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace after the build
            cleanWs()
        }
    }
}


// pipeline {
//     agent any

//     environment {
//         IMAGE_NAME = 'final_02-web:latest'
//     }

//     stages {
//         stage('Clone Code') {
//             steps {
//                 git 'https://github.com/omnhinge/bookstore.git'
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 script {
//                     docker.build(IMAGE_NAME)
//                 }
//             }
//         }

//         stage('Run Tests') {
//     steps {
//         sh "docker run --rm ${IMAGE_NAME} python manage.py test"
//     }
// }

//         stage('Deploy') {
//             when {
//                 branch 'main'
//             }
//             steps {
//                 sh 'docker-compose down && docker-compose up -d --build'
//             }
//         }
//     }
// }


// // pipeline {
// //     agent any

// //     environment {
// //         DJANGO_SETTINGS_MODULE = "bookstore.settings"
// //         PATH = "/usr/local/bin:$PATH"
// //     }

// //     stages {
// //         stage('Clone Repo') {
// //             steps {
// //                 checkout scm
// //             }
// //         }

// //         stage('Build') {
// //             steps {
// //                 sh 'docker-compose build'
// //             }
// //         }

// //         stage('Test') {
// //             steps {
// //                 sh 'docker-compose run --rm web python manage.py test'
// //             }
// //         }

// //         stage('Deploy') {
// //             steps {
// //                 sh 'docker-compose up -d'
// //             }
// //         }
// //     }

// //     post {
// //         always {
// //             echo 'Pipeline finished.'
// //         }
// //         failure {
// //             echo '❌ Pipeline failed. Check test or deployment stage.'
// //         }
// //         success {
// //             echo '✅ Pipeline succeeded.'
// //         }
// //     }
// // }

// pipeline {
//     agent any

//     stages {
//         stage('Clone Code') {
//             steps {
//                 git 'https://github.com/omnhinge/bookstore.git'
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 sh 'docker build -t mydjangoapp .'
//             }
//         }

//         stage('Run Container') {
//             steps {
//                 sh 'docker run -d -p 8000:8000 mydjangoapp'
//             }
//         }
//     }
// }
