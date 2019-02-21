# Timetables_Crawler

### Overview

This web crawler is only for demonstration purposes of the [Scrapy](https://scrapy.org/).

The task is to extract timetables of all the venues in the University of Sydney during 2019.

Following the [Scrapy 1.6 documentation](https://docs.scrapy.org/en/1.6/index.html), the crawler would be optimized and added features step by step.

__It should be noted that the target website use the [Robots exclusion standard](https://en.wikipedia.org/wiki/Robots_exclusion_standard) to limit all areas of it should not be processed by web robots.__

### Example

The script `./example_spider.py` is based on the code in the chapter, [Scrapy at a glance](https://docs.scrapy.org/en/1.6/intro/overview.html#walk-through-of-an-example-spider).

The spider can be ran by using `runspider` command in the directory of repository:

```
runspider example_spider.py -o items.json
```

And it will regenerate a file `items.json` , which contains those items in blue tables on [the example website](https://web.timetable.usyd.edu.au/menu.jsp?siteMap=true).