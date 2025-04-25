pipeline {
    agent any

    environment {
        IMAGE_NAME = 'final_02-web:latest'
    }

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/omnhinge/bookstore.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(IMAGE_NAME)
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image(IMAGE_NAME).inside {
                        sh 'python manage.py test'
                    }
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'docker-compose down && docker-compose up -d --build'
            }
        }
    }
}


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
