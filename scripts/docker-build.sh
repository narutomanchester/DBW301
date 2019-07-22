#!/bin/bash

function build_docker {
    echo "Start building docker..."
    docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
    export TAG=$TRAVIS_BRANCH
    docker build --cache-from $DOCKER_USERNAME/$APP_NAME:$TAG -t $DOCKER_USERNAME/$APP_NAME:$TAG .
    docker push $DOCKER_USERNAME/$APP_NAME:$TAG
}

# when create push request on branch develop
if [[ "$TRAVIS_PULL_REQUEST" = "false" && "$TRAVIS_BRANCH" = "develop" ]] ; then
    build_docker
fi

# when merge pull request on branch master
if [[ "$TRAVIS_PULL_REQUEST" = "false" && "$TRAVIS_BRANCH" = "master" ]] ; then
    build_docker
fi
