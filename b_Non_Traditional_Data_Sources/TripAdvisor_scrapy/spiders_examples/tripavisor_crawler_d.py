<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> ded07d064c5aed9b711c2d26f88645de4a64ab57
# encoding: utf-8

##################################################
# This script corresponds to a "spider" component for the scrapy platform and
# allows to extract different components from the tripadvisor web platform
# d. The spider uses the restaurant's url to call out a new page containing more details.
# Documentation about scrapy and the tutorial used to develop this script
# visit: https://docs.scrapy.org/en/latest/intro/tutorial.html
##################################################
#
##################################################
# Author: Iacopo Testi and Diego Pajarito
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.3.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################


<<<<<<< HEAD
>>>>>>> 64e92099e9ffff4b40980bc3b184583b15f8dff7
=======
>>>>>>> ded07d064c5aed9b711c2d26f88645de4a64ab57
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "tripadvisor_d"
    start_urls = [
        'https://www.tripadvisor.com/Restaurants-g294074-Bogota.html',
    ]

    def parse(self, response):
        for restaurant in response.css("a._15_ydu6b"):
            yield {
<<<<<<< HEAD
<<<<<<< HEAD
                'name': restaurant.css("a._15_ydu6b::text").get(),
                'name_array': restaurant.css("a._15_ydu6b::text").getall(),
                'url': restaurant.attrib['href']
            }

        next_page = response.xpath("//div[@class='unified pagination js_pageLinks']/a[@class='nav next rndBtn ui_button primary taLnk']").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
=======
=======
>>>>>>> ded07d064c5aed9b711c2d26f88645de4a64ab57
                'name_joined': ' '.join(restaurant.css("a._15_ydu6b::text").getall()),
                'url': restaurant.attrib['href']
            }

            # Extract the URL address (relative) to call a different parse method
            restaurant_url = response.urljoin(restaurant.attrib['href'])
            yield scrapy.Request(restaurant_url, callback=self.parse_restaurant)

    # This method searches the restaurant details
    def parse_restaurant(self, response):

        # You need to find new classes to extract data from this page
        yield {

            'title': response.xpath("//h1[@class='ui_header h1']/text()").get(),
            'icon_prize': response.xpath(
                "//div[@class='header_links']/a[@href='/Restaurants-g294074-Bogota.html?pid=6']/text()").get(),
            'average_price': response.xpath(
                "//div[@class='restaurants-detail-overview-cards-DetailsSectionOverviewCard__detailsSummary--evhlS']/div/div[2]/text()").get(),
            'users_rate': response.xpath(
                "//span[@class='restaurants-detail-overview-cards-RatingsOverviewCard__overallRating--nohTl']/text()").get(),
            'number_reviews': response.xpath(
                "//div[@class='restaurants-detail-overview-cards-RatingsOverviewCard__primaryRatingRow--VhEsu']/a[@href='#REVIEWS']/text()").get(),
            'street': response.xpath("//span[@class='street-address']/text()").get()

        }
<<<<<<< HEAD
>>>>>>> 64e92099e9ffff4b40980bc3b184583b15f8dff7
=======
>>>>>>> ded07d064c5aed9b711c2d26f88645de4a64ab57
