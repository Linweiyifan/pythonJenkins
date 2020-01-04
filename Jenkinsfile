pipeline {
    agent { docker 'python' }

    stages {
        stage('build') {
            steps {
                sh "export FLASK_APP=hello.py"
                sh 'echo "测试开始 run run run"'
                sh 'pip install -r requirements.txt'
                sh 'flask run --host=0.0.0.0 &'
                sh 'python test.py'
                sh "curl http://0.0.0.0:5000"
            }
        }
    }
}
