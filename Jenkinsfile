pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Aryan-Bhatt-pro/Jenkins_Project.git'
            }
        }
        stage('Build Code') {
            steps {
                bat "chmod u+x demo.py"
                bat "python3 demo.py"
            }
        }
        stage('Test Code 1') {
            steps {
                bat "chmod u+x PassTestC.py"
                bat "python3 PassTestC.py"
            }
        }
        stage('Test Code 2') {
            steps {
                bat "chmod u+x FailTestC.py"
                bat "python3 FailTestC.py"
            }
        }
    } 
}