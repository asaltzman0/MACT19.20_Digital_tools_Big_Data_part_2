# encoding: utf-8

##################################################
# This script corresponds to a "spider" component for the scrapy platform and
# allows to extract different components from the tripadvisor web platform
<<<<<<< HEAD
<<<<<<< HEAD
=======
# b. The spider calls out and print html objects and the url separately
>>>>>>> 64e92099e9ffff4b40980bc3b184583b15f8dff7
=======
# b. The spider calls out and print html objects and the url separately
>>>>>>> ded07d064c5aed9b711c2d26f88645de4a64ab57
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

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "tripadvisor_b"
    start_urls = [
        'https://www.tripadvisor.com/Restaurants-g294074-Bogota.html',
    ]

    def parse(self, response):
        for restaurant in response.css("a._15_ydu6b"):
<<<<<<< HEAD
<<<<<<< HEAD
=======
            # You can also print out the results using the terminal
>>>>>>> 64e92099e9ffff4b40980bc3b184583b15f8dff7
            name = restaurant.get()
            url = restaurant.attrib['href']
            print(dict(name=name, url=url))
=======
            # You can also print out the results using the terminal
            name = restaurant.get()
            url = restaurant.attrib['href']
            print(dict(name=name, url=url))
>>>>>>> ded07d064c5aed9b711c2d26f88645de4a64ab57
