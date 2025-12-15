pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Environment') {
            steps {
                bat '''
                echo === Jenkins Windows Environment Check ===
                java -version
                git --version
                python --version
                '''
            }
        }
    }
}
