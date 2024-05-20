pipeline {
    agent any
      tools {
      jdk "jdk"
    }
    stages {
        stage('Build') {
            steps {
                // Compile the Java code
                sh 'javac HelloWorld.java'
            }
        }
        stage('Run') {
            steps {
                // Run the Java program
                bat 'start cmd /c "java HelloWorld"'
                echo "Pipeline succeeded"
            }
        }
    }
}

