def installHelm(){
  sh "curl https://baltocdn.com/helm/signing.asc | sudo apt-key add -"
  sh "sudo apt-get install apt-transport-https --yes"
  sh 'echo "deb https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list'
  sh 'sudo apt-get update'
  sh 'sudo apt-get install helm'
}

def installKubectl(){
  sh 'curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"'
  sh 'sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl'
}

    pipeline {

      agent any

      environment {
        registryCredential = credentials('dockerhub')
        containerName = 'timeservice'
        repoName = 'timeservice'
        accountName = 'ragingpuppies'
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

                script {

                  docker.withServer('tcp://host.docker.internal:2375') {

                    sh "docker login -u $registryCredential_USR -p $registryCredential_PSW"

                  }

                } 
          }

        }

        stage('Build') {

          steps {

                script {

                  docker.withServer('tcp://host.docker.internal:2375') {

                    sh "docker build -t $containerName:${env.BUILD_ID} ."

                  }

                } 
          }

        }

        stage('Push') {

          steps {

                  docker.withServer('tcp://host.docker.internal:2375') {

                    sh "docker tag $containerName:${env.BUILD_ID} $accountName/$repoName:${env.BUILD_ID}"
                    sh "docker tag $containerName:${env.BUILD_ID} $accountName/$repoName:latest"

                    sh "docker push $accountName/$repoName"

                    sh "docker rmi -f $accountName/$containerName:${env.BUILD_ID}"
                    sh "docker rmi -f $accountName/$containerName:latest"
                    
                  }

            }

        }

        stage('Deploy') {

          steps {
               container('helm') {
                    sh "helm version"
                }

            } 
        }
      }
    }
