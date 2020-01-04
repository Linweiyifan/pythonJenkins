pipeline {
    agent { docker 'python' }
     environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
    }
    stages {
        stage('build') {
            steps {
                sh 'echo "hello world"'
                sh 'python -m py_compile sources/app.py'
            }
        }
    }
}