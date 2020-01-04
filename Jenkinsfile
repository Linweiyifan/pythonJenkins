pipeline {
    agent { docker 'python:3.7' }
     environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'echo "hello world"'
                sh 'printenv'
                sh 'python app.py'
            }
        }
    }
    post {
    always {
        junit 'build/reports/**/*.xml'
        }
    } 
}