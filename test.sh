#!/usr/bin/env bash

CONTAINER_NAME=outfittr_scraper_images_view
VOLUME_NAME=outfittr_scraper_images

docker run --name $CONTAINER_NAME -v $VOLUME_NAME:/images --rm -itd ubuntu bash > /dev/null &&
docker exec -it $CONTAINER_NAME du -h images &&
docker container stop $CONTAINER_NAME > /dev/null