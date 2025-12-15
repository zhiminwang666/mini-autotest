pipeline {
    agent any

    environment {
        VENV = ".venv"
        PYTHONUTF8 = "1"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup venv & deps') {
            steps {
                bat '''
                echo === Setup Python venv ===
                python -m venv %VENV%
                %VENV%\\Scripts\\python -m pip install --upgrade pip
                %VENV%\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        stage('Start Fake API') {
            steps {
                bat '''
                echo === Start Fake API (FastAPI) ===
                REM 后台启动，日志写到 fake_api.log
                start /B %VENV%\\Scripts\\python -m uvicorn fake_api:app --host 127.0.0.1 --port 8000 > fake_api.log 2>&1
                REM 等待服务起来
                ping 127.0.0.1 -n 6 > nul
                '''
            }
        }

        stage('Run tests') {
            steps {
                bat '''
                echo === Run pytest ===
                %VENV%\\Scripts\\pytest -q --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            echo '=== Publish Allure report ==='
            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'allure-results']]

            echo '=== Archive logs ==='
            archiveArtifacts artifacts: 'fake_api.log', onlyIfSuccessful: false
        }
    }
}
