# Download images
## Enable images pipeline
`ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}`

`IMAGES_STORE = 'tmp/images/'`

## Set the url to the field image_urls
`scraped_info['image_urls'] = ['https://static.runoob.com/images/icon/go.png']`