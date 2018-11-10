FROM python:3.7

WORKDIR /usr/src/outfittr_scraper

# Setup dependencies
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv
RUN pipenv install --system --deploy

# Copy necessary source files
COPY outfittr_scraper outfittr_scraper
COPY scrapy.cfg .

# Run all of the scrapers
CMD scrapy list | xargs -P 0 -n 1 scrapy crawl
