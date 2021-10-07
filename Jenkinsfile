pipeline {
    agent {
        docker {
            image 'ubuntu:focal'
        }
    }
    stages {
        stage ('Build') {
            steps {
                echo 'Testing Jenkinsfile'
                sh 'python3 setup.py check'
            }
        }
    }
}
