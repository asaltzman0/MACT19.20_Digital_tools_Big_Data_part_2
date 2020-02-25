<<<<<<< HEAD
=======
# encoding: utf-8

##################################################
# This script corresponds to a "spider" component for the scrapy platform and
# allows to extract different components from the tripadvisor web platform
# c. The spider calls out to attributes and join them into a single text variable.
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


>>>>>>> 64e92099e9ffff4b40980bc3b184583b15f8dff7
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "tripadvisor_c"
    start_urls = [
        'https://www.tripadvisor.com/Restaurants-g294074-Bogota.html',
    ]

    def parse(self, response):
        for restaurant in response.css("a._15_ydu6b"):
<<<<<<< HEAD
            yield {
                'name': restaurant.css("a._15_ydu6b::text").get(),
                'name_array': restaurant.css("a._15_ydu6b::text").getall(),
=======
            # There are options for minimal text formatting tools
            yield {
                'name': restaurant.css("a._15_ydu6b::text").get(),
                'name_array': restaurant.css("a._15_ydu6b::text").getall(),
                'name_joined': ' '.join(restaurant.css("a._15_ydu6b::text").getall()),
>>>>>>> 64e92099e9ffff4b40980bc3b184583b15f8dff7
                'url': restaurant.attrib['href']
            }