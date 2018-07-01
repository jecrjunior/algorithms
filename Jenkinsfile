pipeline {
  agent any
  stages {
    stage('Pylint') {
      steps {
        sh 'pylint ./algorithms/algorithms'
      }
    }
    stage('Pytest') {
      steps {
        sh 'pytest ./algorithms/tests'
      }
    }
  }
}