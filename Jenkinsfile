pipeline {
    agent any
      tools {
      jdk "jdk"
    }
    stages {
        stage('Build') {
            steps {
                // Compile the Java code
                bat 'javac HelloWorld.java'
            }
        }
        stage('Run') {
            steps {
                // Run the Java program
                bat 'java HelloWorld'
                echo "Pipeline succeeded"
            }
        }
    }
}

