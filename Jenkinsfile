pipeline {
 agent any
    tools {
        // Specify the JDK tool installation name
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
     
        stage('Build docker image') {
            steps {
                // Build Docker image
               script {
                    bat 'docker build -t MyjavaImage .'
                }
           }
        }
    }
}
