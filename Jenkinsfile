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

kubeconfig(caCertificate: '''-----BEGIN CERTIFICATE-----
MIIDBjCCAe6gAwIBAgIBATANBgkqhkiG9w0BAQsFADAVMRMwEQYDVQQDEwptaW5p
a3ViZUNBMB4XDTIxMTEyODA4MzQyMloXDTMxMTEyNzA4MzQyMlowFTETMBEGA1UE
AxMKbWluaWt1YmVDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANRE
UTLXNMQnSvbC0/R0I48RmzW4f/Gn0k42tilDv3w4qBScJK2GJrF7QKFj1ykeRHP/
qruHLAs1XNBqcCjl4T7oTOsIzzrs05joXFHYY+yS2YhaJ3mDlsHh0NiBL4ESRRbs
zT1zgFgdHbBA7r2ruSIzb7ztqh8g+aw9T9Qd5yXDONo9+Z/fnMaUL1OoCfrSM483
Eph+6mKmoGXf+hrWu5KllP5+mY78zVn35RNhyNxSCUBX/++1cr8/zK1q30eVBeAQ
hW6DkASH9ZgNIpydMm1BP5mz3pIBPehGSd4I5NGeOFtQxstJF7If4d2Z2q9//SPp
09reP2ViAPjVN2Vu6yECAwEAAaNhMF8wDgYDVR0PAQH/BAQDAgKkMB0GA1UdJQQW
MBQGCCsGAQUFBwMCBggrBgEFBQcDATAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQW
BBRO0VlapoA9LfYIDeRu63uJBzhaNTANBgkqhkiG9w0BAQsFAAOCAQEAfPwJKQbr
vXnsLjjmNQhrZGhhiF0Yr7VWCkR4y70Px1eNF1pryRfk6bPfUGTb2Tdyc3/kVFQ7
LXCpy71ghGV4n/GDZezJZpVYD365O4PeR9BstPCS+c7Txex+coBmdihxSU5Dd6eM
UlmaliKaUl5j/BfvokrY7KZKgFQtQZQvx1sf33rbbEsSQ+SmrgIbJygDMzkTaex9
gsrHWg0PFwy3EBj4OGD6kkqJKa1efhCRhy74w387g9k3a5GvrjEQuUt4wJbpauED
Dqy8WfO6izm8kRrOsmVHcZcqlQ+dIedXRO9P/Pmoe7l8KizWw1ZNwnfHHz9JSBj6
+O8yEvIBIwErcw==
-----END CERTIFICATE-----''', credentialsId: '735cd2d7-18ab-4ba8-b584-e9c87a51fee9', serverUrl: 'https://kubernetes.default') {
    sh 'kubectl get nodes'
}
    

            


          }
        }

    }
}