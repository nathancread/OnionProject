import onion

def prepareOnion():
    links = onion.scrape('https://www.theonion.com/')
    links += onion.scrape('https://politics.theonion.com/')
    links += onion.scrape('https://sports.theonion.com/')
    links += onion.scrape('https://local.theonion.com/')
    links += onion.scrape('https://entertainment.theonion.com/')
    newLinks = onion.findUniqueLinks('D:/OnionProject/savedlinks.txt',links)
    return newLinks

#onion.openList(newLinks)
def prepareBee():
    links = onion.scrape('https://babylonbee.com/')
    links += onion.scrape('https://babylonbee.com/news')
    links += onion.scrape('https://babylonbee.com/news/categories/christian-living')
    links += onion.scrape('https://babylonbee.com/news/categories/celebs')
    links += onion.scrape('https://babylonbee.com/news/categories/politics')
    links += onion.scrape('https://babylonbee.com/news/categories/church')
    links += onion.scrape('https://babylonbee.com/news/categories/entertainment')
    newLinks = onion.findUniqueLinks('D:/OnionProject/beeLinks.txt',links)
    return newLinks

links = prepareOnion()
onion.openList(links)

print('well done')