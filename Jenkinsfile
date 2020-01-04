pipeline {
    agent { docker 'python' }

    stages {
        stage('build') {
            steps {
                sh "export FLASK_APP=hello.py"
                sh 'echo "测试开始 run run run"'
                sh 'pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple'
                sh 'flask run --host=0.0.0.0'
                sh "curl http://0.0.0.0:5000"
                sh 'python test.py'
            }
        }
    }
}
