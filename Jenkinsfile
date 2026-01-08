pipeline {
	
        agent any 

	environment {
 	     IMAGE_NAME = "cicd-demo:latest"
	}
	
	stages {
	     stage('Clone code'){
		steps{
		    git url : 'https://github.com/BabuLahade/Production-Grade-CI-CD-Platform-on-AWS.git', branch: 'main'
		}
	     }
             stage('Build Docker Image'){
                steps{
                    sh ' docker build -t $IMAGE_NAME -f  docker/Dockerfile .'
                }
             }
	     stage('Deploy to Kubernetes'){
		steps{
		    sh '''
		    sed -i "s|IMAGE_NAME|$IMAGE_NAME|g" kubernetes/deployment.yml
		    kubectl apply -f . 
		    '''
		}
	     }
	}
}
