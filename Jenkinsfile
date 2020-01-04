pipeline {
    agent { docker 'python' }
     environment {
        export FLASK_APP=hello.py
    }
    stages {
        stage('build') {
            steps {
                sh 'echo "测试开始 run run run"'
                sh 'pip install -r requirements.txt'
                sh 'flask run'
                sh 'python test.py'
            }
        }
    }
}