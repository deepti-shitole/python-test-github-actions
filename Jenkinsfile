pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Compile the Java file
                sh 'javac HelloWorld.java'
            }
        }
        stage('Test') {
            steps {
                // Run the compiled Java program
                sh 'java HelloWorld'
            }
        }
    }
}
