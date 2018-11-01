# Outfitter Scraper

## About

This is a work in progress.

## Usage

In order to run the project, execute: `./run.sh` in the root of the project 
folder. Please ensure that Docker is installed, and, if necessary for your OS, 
that the Docker daemon is running.

## Testing

In order to test the project quickly, please ensure that you have successfully 
run the project at least once. Then, execute: `./test.sh`. You should see output
similar to the following:

```
(outfitter_scraper) ❯ ./test.sh
20M     images/tops
3.3M    images/bottoms
23M     images
```

The above output shows the number of megabytes consumed by scraped images of 
each respective clothing type (i.e, tops and bottoms).