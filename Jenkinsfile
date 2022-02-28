def CONTAINER_NAME="$JOB_NAME"
def CONTAINER_TAG="$BUILD_TAG"

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
    /*
     stage('Upload') {
        dir('path/to/your/project/workspace'){
            pwd(); //Log current directory
            withAWS(region:'yourS3Region',credentials:'yourIDfromStep2') {
                 def identity=awsIdentity();//Log AWS credentials
                // Upload files from working directory 'dist' in your project workspace
                s3Upload(bucket:"yourBucketName", workingDir:'dist', includePathPattern:'**/*');
            }
        };
    }
    */
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
