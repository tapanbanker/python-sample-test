def CONTAINER_NAME="$JOB_NAME"
def CONTAINER_TAG="$BUILD_TAG"
def ARTIFACTS_FOLDER="/tmp/${JOB_NAME}_artifacts"
def CONTAINER_WORKSPACE="/app"

node {
    stage('Initialize'){
      def dockerHome = tool 'docker'
      def imageName = "$CONTAINER_NAME:$CONTAINER_TAG"
      env.PATH = "${dockerHome}/bin:${env.PATH}"
      env.DOCKER_HOST = 'tcp://172.31.10.107:4243'
    }
    stage('Git Clone') {
      git([url: 'https://github.com/tapanbanker/python-sample-test.git', branch: 'main', credentialsId: ''])
    }
    stage("Image Prune"){
        imagePrune(CONTAINER_NAME)
    }
    stage('Image Build'){
        imageBuild(CONTAINER_NAME, CONTAINER_TAG)
    }
    stage('Run Tests'){
        execInContainer(CONTAINER_NAME, CONTAINER_TAG, "pipenv run test")
    }
    stage('Archive and Upload'){
        zipAndUpload(CONTAINER_NAME, CONTAINER_TAG, ARTIFACTS_FOLDER, CONTAINER_WORKSPACE);
    }
}
def imagePrune(containerName){
    try {
        sh "docker image prune -f"
        sh "docker stop $containerName"
        sh "docker rm $containerName"
    } catch(error){}
}
def imageBuild(containerName, tag){
    sh "docker build -t $containerName:$tag -t $containerName --pull --no-cache ."
    echo "Image build complete"
}
def execInContainer(containerName, tag, command){
    sh "docker run --name $containerName $containerName:$tag /bin/bash -c \"$command\""
    sh "docker rm $containerName"
    echo "Command $command execution complete"
}

def zipAndUpload(containerName, tag, artifacts_folder, container_workspace){
    sh "mkdir -p ${artifacts_folder}"
    sh "docker run --name $containerName $containerName:$tag /bin/bash -c \"rm -rf .git && mkdir -p /artifacts && tar -zcvf /artifacts/gzipped.tar.gz ${container_workspace} && ls /artifacts\" "
    sh "docker cp $containerName:/artifacts/gzipped.tar.gz ${artifacts_folder}"
    sh "cp ${artifacts_folder}/gzipped.tar.gz /var/jenkins_home/workspace/${containerName}/"
    withAWS(region:'us-east-1',credentials:'aws_test') {
        s3Upload(bucket:"test-tapan-temp", file:'gzipped.tar.gz', path:'gzipped.tar.gz');
    }
    sh "docker rm $containerName"
    echo "Archive created and uploaded"
}
