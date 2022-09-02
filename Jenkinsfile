pipeline {
    agent any

    stages{
        stage ('Build Image'){
            steps {
                script {
                    dockerapp = docker.build("psicomotricidade", '-f ./dockerfile .')
                    
                }
            }
        }
    }
}