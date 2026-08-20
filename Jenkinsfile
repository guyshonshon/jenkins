pipeline {
    agent any

    environment {
        APP_VERSION = '1.0'
        APP_NAME = 'guy'
        DOCKER_REPO = 'guyshonshon@jenkins'
        FILE_TO_TEST = './build-info.txt'
    }

    stages {

        stage('Build') {
            steps {
                echo '======= build stage ========'
                echo "APP_NAME=${APP_NAME}, APP_VERSION=${APP_VERSION}, DOCKER_REPO=${DOCKER_REPO}"
                sh 'echo "app" > app.txt'
                // idk if this should be in multi-lines but w.e
                sh 'echo "APP_NAME=${APP_NAME}\nBUILD_NUMBER=${BUILD_NUMBER}\nDATE=$(date)\n" > build-info.txt'
            }
        }

        stage('Parallel Tests') {
            parallel {

                stage('file test') {
                    steps {
                        //-f returns exit 0 on success and exit 1 on failure
                        sh 'test -f "app.txt"' 
                    }
                }

                stage('build-info test') {
                    steps {
                        sh 'python3 script.py "$FILE_TO_TEST" "$BUILD_NUMBER"'
                    }
                }
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