pipeline {
    agent any

    stages{
        stage("Stopping old container"){
            steps{
                sh """
                    docker stop psicomotricidade
                """
            }
        }
        stage("Removing old container"){
            steps{
                sh """
                    docker rm psicomotricidade
                """
            }
        }
        stage("deleting old image"){
            steps{
                sh """
                    docker rmi psicomotricidade -f
                """
            }
        }
        stage("Build new Image"){
            steps {
                sh """
                    docker build -t psicomotricidade .
                """
            }
        }
        stage("run container"){
        steps{
        sh """
            docker run -d --name psicomotricidade -p 80:8000 psicomotricidade
        """
        }
        }
    }
}



