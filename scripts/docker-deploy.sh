#!/bin/bash

export TAG=$TRAVIS_BRANCH
function deploy_app {
    echo "Start deploying docker..."
    ssh -i ./deploy_key $SERVER_DEV -o StrictHostKeyChecking=no "cd $PROJECT_PATH && echo \"$DOCKER_PASSWORD\" | docker login --username \"$DOCKER_USERNAME\" --password-stdin && docker pull \"$DOCKER_USERNAME\"/\"$APP_NAME\":\"$TAG\" && docker-compose up -d"
}

# when create push request on branch develop
if [[ "$TRAVIS_PULL_REQUEST" = "false" && "$TRAVIS_BRANCH" = "develop" ]] ; then
    deploy_app
fi

# # when merge pull request on branch master
# if [[ "$TRAVIS_PULL_REQUEST" = "false" && "$TRAVIS_BRANCH" = "master" ]] ; then
#     deploy_app
# fi
