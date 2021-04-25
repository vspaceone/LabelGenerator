pipeline {
    agent any
    environment {
        dockerImage = ''
        DOCKER_REGISTRY = 'https://docker.vspace.one'
        DOCKER_CREDENTIALS = 'system-nexus-deploy'
        DOCKER_IMAGE = 'docker.vspace.one/labelgenerator'

        RELEASE_STAGE_WEBHOOK = credentials('vspaceone-webhook-labelgenerator-release')
        MASTER_STAGE_WEBHOOK = credentials('vspaceone-webhook-labelgenerator')
        BETA_STAGE_WEBHOOK = credentials('vspaceone-webhook-labelgenerator-dev')
    }
    stages {
        stage('Build image') {
            steps {
                script {
                    dockerImage = docker.build("$DOCKER_IMAGE")
                }
            }
        }
        stage('Push release') {
            when { buildingTag }
            steps {
                script {
                    docker.withRegistry( DOCKER_REGISTRY, DOCKER_CREDENTIALS ) {
                        dockerImage.push("$TAG_NAME")
                        dockerImage.push("latest")
                    }                    
                }
            }
        }
        stage('Push latest image') {
            when {
                expression { env.BRANCH_NAME == 'master' }
            }
            steps {
                script {
                    docker.withRegistry( DOCKER_REGISTRY, DOCKER_CREDENTIALS ) {
                        dockerImage.push("master")
                    }                    
                }
            }
        }
        stage('Push beta image') {
            when {
                expression { env.BRANCH_NAME == 'develop' }
            }
            steps {
                script {
                    docker.withRegistry( DOCKER_REGISTRY, DOCKER_CREDENTIALS ) {
                        dockerImage.push("develop")
                    }
                }
            }
        }
        stage('Send release webhooks') {
            when {
                when { buildingTag() }
            }
            steps {
                sh "curl $RELEASE_STAGE_WEBHOOK"
            }
        }
        stage('Send master webhooks') {
            when {
                expression { env.BRANCH_NAME == 'master' }
            }
            steps {
                sh "curl $MASTER_STAGE_WEBHOOK"
            }
        }
        stage('Send beta webhooks') {
            when {
                expression { env.BRANCH_NAME == 'develop' }
            }
            steps {
                sh "curl $BETA_STAGE_WEBHOOK"
            }
        }
    }
}