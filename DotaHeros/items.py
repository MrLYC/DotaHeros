# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DotaSolutionItem(scrapy.Item):
    Name = scrapy.Field()
    Solutions = scrapy.Field()


class DotaHerosItem(scrapy.Item):
    Name = scrapy.Field()
    Position = scrapy.Field()

    DPS = scrapy.Field()
    Push = scrapy.Field()
    Gank = scrapy.Field()
    Support = scrapy.Field()
    Tank = scrapy.Field()

    HP = scrapy.Field()
    MP = scrapy.Field()
    BiuDistance = scrapy.Field()
    Speed = scrapy.Field()
    Attack = scrapy.Field()
    AttackSpeed = scrapy.Field()
    Armour = scrapy.Field()
    Power = scrapy.Field()
    Alacrity = scrapy.Field()
    Intelligence = scrapy.Field()

    Advantage = scrapy.Field()
    Disadvantage = scrapy.Field()

    Partner = scrapy.Field()
    Enemy = scrapy.Field()

    BuildSolution = scrapy.Field()
    EquipmentSolution = scrapy.Field()
