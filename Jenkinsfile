    pipeline {

      agent any

      environment {
        registryCredential = 'dockerhub'
      }

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

                  docker.withServer('tcp://host.docker.internal:2375') {
                    def dockerImage = docker.build("time-service:${env.BUILD_ID}")
                    docker.withRegistry("", registryCredential) {
                      dockerImage.push()
                    }
                    
                  }

                  sh 'docker rmi -f ${env.BUILD_DISPLAY_NAME}:${env.BUILD_ID}'

                } 
            } 
        }
      }
    }
