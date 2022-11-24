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
                sh "chmod u+x demo.py"
                sh "python demo.py"
            }
        }
        stage('Test Code 1') {
            steps {
                sh "chmod u+x PassTestC.py"
                sh "python PassTestC.py"
            }
        }
        stage('Test Code 2') {
            steps {
                sh "chmod u+x FailTestC.py"
                sh "python FailTestC.py"
            }
        }
    } 
}