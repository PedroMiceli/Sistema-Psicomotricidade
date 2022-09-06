pipeline {
    agent {label "linux"}

    stages{
        stage ('Build Image'){
            steps {
                sh """
                    docker build -t psicomotricidade .
                """
            }
        }
        stage("run"){
        steps{
        sh """
            docker run --rm psicomotricidade
        """
        }
        }
    }
}