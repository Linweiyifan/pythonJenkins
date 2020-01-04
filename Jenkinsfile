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
                sh 'python app.py'
            }
        }
    }
}