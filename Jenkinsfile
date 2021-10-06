pipeline {
    agent any
    stages {
        stage ('Build') {
            steps {
                echo 'Testing Jenkinsfile'
                sh 'python3 setup.py check'
            }
        }
    }
}
