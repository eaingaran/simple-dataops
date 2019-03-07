pipeline {
    environment {
        isDeploymentSuccess = ''   
    }
    agent any
    tools {
      maven 'maven'
      jdk 'jdk1.8.0'
    }
    stages {
        stage('DryRun') {
            steps {
                echo 'Testing the scrips on a temporary database...'
                sh 'mvn liquibase:dropAll'
                sh 'mvn liquibase:update'
                sh 'mvn liquibase:rollback -Dliquibase.rollbackCount=10000000'
            }
        }
        stage('CreateSQL') {
            steps {
                echo 'Creating update SQL from scripts..'
                sh 'mvn clean liquibase:updateSQL'
                sh 'mkdir build && cp target/liquibase/migrate.sql build/update.sql'
            }
        }
        stage('RollbackSQL') {
            steps {
                echo 'Creating rollback SQL from scripts..'
                sh 'mvn clean liquibase:futureRollbackSQL'
                sh 'cp target/liquibase/migrate.sql build/rollback.sql'
            }
        }
        stage('ArchiveCreation') {
            steps {
                echo 'Creating a tar.gz....'
                sh 'tar -czvf sample-devops-0.0.1.${BUILD_ID}.tar.gz build/'
            }
        }
        stage('ArchiveUpload') {
            steps {
                echo 'Deploying tar file to artifactory....'
                sh 'curl -uadmin:AP3k8uCck9Xxw1GG3i3yz2rq4Kz -T sample-devops-0.0.1.${BUILD_ID}.tar.gz "http://34.221.104.185:8081/artifactory/libs-snapshot/xyz/aingaran/dataops/sample-devops-0.0.1.${BUILD_ID}.tar.gz"'
                script {
                    try {
                        sh 'mvn -e -X deploy:deploy-file -DpomFile=pom.xml \
                              -Dfile=sample-devops-0.0.1.${BUILD_ID}.tar.gz \
                              -DrepositoryId=central \
                              -Durl=http://34.221.104.185:8081/artifactory/libs-snapshot/ \
                              -Dpackaging=tar.gz'
                    } catch(Exception e)    {
                        //echo e
                        echo 'couldnt upload via maven deploy'
                    }
                }
            }
        }
        stage('DeploySQL') {
            steps {
                echo 'Deploying....'
                sh './tools/setup.sh'
                script {
                  isDeploymentSuccess = sh(script: 'python execute_sql.py localhost admin password build/update.sql', returnStdout: true)
                }
            }
        }
        stage('DeployRollbackSQL') {
            when {
                expression { isDeploymentSuccess == 'Failed' }
            }
            steps{
                echo 'Deploying Rollback....'
                script {
                  sh 'python execute_sql.py localhost admin password build/rollback.sql'
                }
            }
        }
        stage('TestDatabase') {
            steps {
                echo 'Coming Soon....'
            }
        }
    }
}
