pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo '======= build stage ========'
                echo 'Building application...'
                sh 'echo "hey app is now alive" > app.txt'
            }
        }

        stage('Test') {
            steps {
                echo '======= test stage ========'
                echo 'Running tests...'
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