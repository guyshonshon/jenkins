pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo '======= build stage ========'
                echo 'Building application...'
            }
        }

        stage('Test') {
            steps {
                echo '======= test stage ========'
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                echo '======= deploy stage ========'
                echo 'Deploying application...'
            }
        }
    }
    post {
        always {
            deleteDir()
        }
    }
}