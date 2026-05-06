pipeline {

    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'YOUR_GITHUB_REPO_LINK'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest -n 4 --alluredir=allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            }
        }
    }

    post {

        always {

            archiveArtifacts artifacts: 'screenshots/*.png', allowEmptyArchive: true

            archiveArtifacts artifacts: 'logs/*.log', allowEmptyArchive: true
        }
    }
}