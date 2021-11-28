    pipeline {
      agent any
      stages{
        stage('Initialize'){
          steps {
                script{
                  def dockerHome = tool 'docker-builder'
                  env.PATH = "${dockerHome}/bin:${env.PATH}"
                }
          }
        }
        stage('Build and Push Docker Image...') {
          steps {
                script {
         
                  def dockerImage = docker.build("time-service:${env.BUILD_ID}")
                        
                  dockerImage.push()

                  sh 'docker rmi -f ${env.BUILD_DISPLAY_NAME}:${env.BUILD_ID}'

                } 
            } 
        }
     }
    }
