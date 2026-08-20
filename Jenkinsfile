pipeline {
    agent any

    environment {
        APP_VERSION = '1.0'
        APP_NAME = 'guy'
        DOCKER_REPO = 'guyshonshon@jenkins'
        FILE_TO_TEST = 'script.py'
    }

    stages {

        stage('Build') {
            steps {
                echo '======= build stage ========'
                echo "APP_NAME=${APP_NAME}, APP_VERSION=${APP_VERSION}, DOCKER_REPO=${DOCKER_REPO}"

                sh 'echo "hey app is now alive" > app.txt'
            }
        }

        stage('Test') {
            steps {
                echo '======= test stage ========'
                echo "Tests run on pipeline '${JOB_NAME}', build: '${BUILD_NUMBER}'"
                sh 'test -f app.txt'
            }
            
        }

        stage('Deploy') {
            steps {
                echo '======= deploy stage ========'
                echo 'Deploying application...'
                sh 'mkdir -p deploy'
                sh 'cp app.txt deploy/'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}