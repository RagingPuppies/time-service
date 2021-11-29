  podTemplate(containers: [
    containerTemplate(name: 'helm', image: 'dtzar/helm-kubectl', command: 'sleep', args: '99d'),
    containerTemplate(name: 'docker', image: 'alpinelinux/docker-cli', command: 'sleep', args: '99d')
  ])
  
  {
    node(POD_LABEL) {

      def containerName = 'timeservice'
      def accountName = 'ragingpuppies'
      def repoName = 'timeservice'

        stage('login') {
            container('docker') {
                script {
                    docker.withServer('tcp://host.docker.internal:2375') {
                        withCredentials([[$class: 'UsernamePasswordMultiBinding', 
                            credentialsId: 'dockerhub',
                            usernameVariable: 'registryCredential_USR', 
                            passwordVariable: 'registryCredential_PSW']]) {
                            sh "docker login -u $registryCredential_USR -p $registryCredential_PSW"
                        }
                    }
                }
            } 
        }

        stage('Build') {
            git 'https://github.com/RagingPuppies/time-service.git'
            container('docker') {
                script {
                    docker.withServer('tcp://host.docker.internal:2375') {
                            sh "docker build -t $containerName:${env.BUILD_ID} ."
                    }
                }
            } 
        }

        stage('Push') {
            git 'https://github.com/RagingPuppies/time-service.git'
            container('docker') {
                script {
                    docker.withServer('tcp://host.docker.internal:2375') {
                        sh "docker tag $containerName:${env.BUILD_ID} $accountName/$repoName:${env.BUILD_ID}"
                        sh "docker tag $containerName:${env.BUILD_ID} $accountName/$repoName:latest"
                        sh "docker push $accountName/$repoName"
                        sh "docker rmi -f $accountName/$containerName:${env.BUILD_ID}"
                        sh "docker rmi -f $accountName/$containerName:latest"
                    }
                }
            } 
        }

        stage('Deploy') {
          container('helm') {
              sh "helm --help"
    
              withKubeConfig([credentialsId: 'kubeconfig-file'
                              ]) {
                sh 'kubectl get pods'
              }

            


          }
        }

    }
}