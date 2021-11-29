    pipeline {

      agent any

      environment {
        registryCredential = credentials('dockerhub')
        containerName = 'timeservice'
        repoName = 'timeservice'
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

        stage('Login'){

          steps {

                sh "docker login -u $registryCredential_USR -p $registryCredential_PSW"

          }

        }

        stage('Build') {

          steps {

                script {

                  docker.withServer('tcp://host.docker.internal:2375') {

                    sh "docker build -t ragingpuppies/$containerName:${env.BUILD_ID} ."

                  }

                } 
          }

        }

        stage('Push') {

          steps {

                script {

                  docker.withServer('tcp://host.docker.internal:2375') {

                    sh "docker tag $containerName:${env.BUILD_ID} ragingpuppies/$repoName:${env.BUILD_ID}"

                    sh "docker push ragingpuppies/$repoName $containerName:${env.BUILD_ID}"
                    
                  }

                  sh "docker rmi -f $containerName:${env.BUILD_ID}"

                } 
            } 
        }
      }
    }
