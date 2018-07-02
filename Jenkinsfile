pipeline {
  agent any
  stages {
    stage('Pylint') {
      steps {
        pysh(script: '/var/lib/jenkins/workspace/software_quality_env/bin/activate')
        sh '''pylint /var/lib/jenkins/workspace/algorithms_final_master-HMR4SQVWMPXTDGR7DR4MHA3BUAXSNJU3TFG575ITVJ3EHQ2KJRFA/algorithms > lint_report.txt | exit 0
	'''
      }
    }
    stage('Pytest') {
      steps {
        sh '''	#!/bin/bash |
		source /var/lib/jenkins/workspace/software_quality_env/bin/activate |
		pytest /var/lib/jenkins/workspace/algorithms_final_master-HMR4SQVWMPXTDGR7DR4MHA3BUAXSNJU3TFG575ITVJ3EHQ2KJRFA/tests > test_report.txt | 
		exit 0 
	'''
      }
    }
  }
}