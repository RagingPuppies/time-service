        stage('Build and Push Docker Image...') {
          steps {
                script {
         
                  def dockerImage = docker.build("${env.BUILD_DISPLAY_NAME}:${env.BUILD_ID}")
                        
                  dockerImage.push()

                  sh 'docker rmi -f ${env.BUILD_DISPLAY_NAME}:${env.BUILD_ID}'

                } 
            } 
        }