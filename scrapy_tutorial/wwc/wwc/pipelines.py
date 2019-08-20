# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class HouseDotGovDemsOnlyPipeline(object):
    """
    Pipeline to only return democratic
    representatives.
    """
    def __init__(self):
        self.dem_count = 0
        self.repub_count = 0
        self.other_count = 0

    def process_item(self, item, spider):
        if item.get("party") == "D":
            self.dem_count += 1
            return item

        if item.get("party") == "R":
            self.repub_count += 1
        else:
            self.other_count += 1
        raise DropItem("Only keeping democrats")

    def close_spider(self, spider):
        print("---------------PIPELINE PROCESSING COMPLETE---------------")
        print("Democrats: {}".format(self.dem_count))
        print("Republicans: {}".format(self.repub_count))
        print("Other: {}".format(self.other_count))


class HouseDotGovDupesPipeline(object):
    """
    Pipeline to remove duplicate reps
    """
    def __init__(self):
        self.websites = set()
        self.dropped_sites = set()

    def process_item(self, item, spider):
        """
        If the item is already in the set we have,
        then don't keep it again
        """
        website = item['website']
        if website in self.websites:
            self.dropped_sites.add(website)
            raise DropItem("Duplicate representative. Skipping: {}".format(item))
        else:
            self.websites.add(website)
            return item

    def close_spider(self, spider):
        print("---------------PIPELINE PROCESSING COMPLETE---------------")
        print("Sites count: {}".format(len(self.websites)))
        print("Dropped sites: {}".format(self.dropped_sites))
