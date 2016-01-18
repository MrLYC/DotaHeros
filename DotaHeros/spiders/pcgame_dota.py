#!/usr/bin/env python
# coding: utf-8
# create at: 2016-01-17 11:44:18

import scrapy

from DotaHeros.items import DotaHerosItem, DotaSolutionItem


class DotaHerosSpider(scrapy.Spider):
    name = "DotaHeros"
    allowed_domains = ["pcgames.com.cn"]
    start_urls = [
        "http://fight.pcgames.com.cn/dota2/heros/",
    ]

    def parse(self, response):
        for i in response.css("ul.picUl>li"):
            yield scrapy.Request(
                i.xpath("a/@href").extract_first(),
                callback=self.parse_hero,
            )

    def parse_hero(self, response):
        hero = DotaHerosItem()
        hero["Name"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[1]/a[1]/text()'
        ).extract_first()
        hero["Position"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[2]/text()'
        ).re(ur'[：\s](\S+)')

        hero["DPS"], hero["Push"], hero["Gank"], hero["Support"], hero["Tank"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[1]/div[2]/div[1]/span/text()'
        ).re(ur'：(\d+)')

        hero["HP"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/text()'
        ).re(r'/(\d+)')[0]
        hero["MP"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/text()'
        ).re(r'/(\d+)')[0]
        hero["BiuDistance"], hero["Speed"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[3]/text()'
        ).re(ur"：(\d+)")
        hero["Attack"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/p[1]/span[1]/text()'
        ).re(r' (.+)$')[0]
        hero["AttackSpeed"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/p[2]/span[1]/text()'
        ).re(r' (.+)$')[0]
        hero["Armour"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/p[3]/span[1]/text()'
        ).re(r' (.+)$')[0]
        hero["Power"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/p[1]/span[2]/text()'
        ).re(r' (.+)$')[0]
        hero["Alacrity"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/p[2]/span[2]/text()'
        ).re(r' (.+)$')[0]
        hero["Intelligence"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/p[3]/span[2]/text()'
        ).re(r' (.+)$')[0]

        hero["Advantage"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/text()'
        ).extract_first()
        hero["Disadvantage"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/text()'
        ).extract_first()

        hero["Partner"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[2]/div[1]/dl[1]/dd/div/i[1]/a/span/text()'
        ).extract()
        hero["Enemy"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[2]/div[1]/dl[2]/dd/div/i[1]/a/span/text()'
        ).extract()

        hero["BuildSolution"] = build_solution = DotaSolutionItem()
        build_solution["Name"] = u"加点方案"
        build_solution["Solutions"] = response.xpath(
            '//*[@id="artArea"]/div[2]/div[1]/div[2]/div[2]/div[2]/ul/li/img/@alt'
        ).extract()
        hero["EquipmentSolution"] = [
            DotaSolutionItem(
                Name=node.xpath('span/text()').extract_first(),
                Solutions=node.xpath("a/img/@alt").extract(),
            )
            for node in response.xpath(
                '//*[@id="artArea"]/div[2]/div[1]/div[2]/div[3]/div[2]/ul/li'
            )
        ]

        yield hero
