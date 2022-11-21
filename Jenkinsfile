pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/harsh788/Jenkins-Lab.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x fibonacci.py"
                sh "fibonacci.py"
            }
        }
        stage('Test Code Passed') {
            steps {
                sh "chmod u+x test1.py"
                sh "test1.py"
            }
        }
        stage('Test Code Failed') {
            steps {
                sh "chmod u+x test2.py"
                sh "test2.py"
            }
        }
    } 
}