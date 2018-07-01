pipeline {
  agent any
  stages {
    stage('Pylint') {
      steps {
        sh '''pylint /var/lib/jenkins/workspace/algorithms_final_master-HMR4SQVWMPXTDGR7DR4MHA3BUAXSNJU3TFG575ITVJ3EHQ2KJRFA/algorithms
'''
      }
    }
    stage('Pytest') {
      steps {
        sh 'pytest /var/lib/jenkins/workspace/algorithms_final_master-HMR4SQVWMPXTDGR7DR4MHA3BUAXSNJU3TFG575ITVJ3EHQ2KJRFA/tests '
      }
    }
  }
}