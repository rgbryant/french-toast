pipeline {
    agent any
    stages {
        stage ('Build Environment'){
            steps {
                def environment = docker.build 'french-toast'
                environment.inside {
                    stage "Build2"
                        echo 'Testing inside stage'
                        sh' python3 setup.py check'
                }
            }
        }
        stage ('Build') {
            steps {
                echo 'Testing Jenkinsfile'
                sh 'python3 setup.py check'
            }
        }
    }
}
