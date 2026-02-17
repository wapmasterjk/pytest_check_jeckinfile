pipeline{
    agent any
    stages{
        stage('Checkout Code'){
            steps{
                git branch:'main', url:'https://github.com/wapmasterjk/pytest_check_jeckinfile.git'
            }
        }
        stage('Setup Python'){
            steps{
            sh 'python -m venv .venv'
            }
        }
        stage('Install dependencies') {
            steps{
                sh '
                .venv/Script/activate
                pip install -r requirements.txt
                '
            }
        }
        stage('Run Test'){
            steps{
                sh 'pytest'
            }
        }
    }
}
