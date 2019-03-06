pipeline {
    agent any
    tools {
      maven 'maven'
      jdk 'jdk8'
    }
    stages {
        stage('DryRun') {
            steps {
                echo 'Testing the scrips on a temporary database...'
            }
        }
        stage('CreateSQL') {
            steps {
                echo 'Testing..'
            }
        }
        stage('RollbackSQL') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('ArchiveCreation') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('ArchiveUpload') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('DeploySQL') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('DeployRollbackSQL') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('TestDatabase') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
