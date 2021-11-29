  podTemplate(containers: [
    containerTemplate(name: 'helm', image: 'alpine/helm', command: 'sleep', args: '99d'),
    containerTemplate(name: 'docker', image: 'alpinelinux/docker-cli', command: 'sleep', args: '99d')
  ])
  
  {
    node(POD_LABEL) {
      def containerName = 'timeservice'
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
            container('docker') {
                script {
                    docker.withServer('tcp://host.docker.internal:2375') {
                            sh "docker build -t $containerName:${env.BUILD_ID} ."
                    }
                }
            } 
        }

        stage('Build Docker image') {
          container('helm') {
            sh "helm --help"
          }
        }

    }
}