class Pagination:
    def __init__(self, current_page, last_page, per_page, has_more_pages,
                 first_item, last_item, total, count):
        self.current_page = current_page
        self.last_page = last_page
        self.per_page = per_page
        self.has_more_pages = has_more_pages
        self.first_item = first_item
        self.last_item = last_item
        self.total = total
        self.count = count


    def show_pagination_details(self):
        print "\n================[ Product ]====================="
        print "current_page . . . . . . . . . : ", self.current_page
        print "last_page . . . . . . . . : ", self.last_page
        print "per_page . . . . .: ", self.per_page
        print "has_more_pages . . . . . . : ", self.has_more_pages
        print "first_item . . . . . : ", self.first_item
        print "last_item . . .  . .: ", self.last_item
        print "total . . . . . : ", self.total
        print "count . . .  . .: ", self.count
        print "================================================\n"


class Product:
    def __init__(self, id, name, dispensary_id, dispensary_name,
                 canabis_brand, canabis_strain, category, subcategory,
                 thc_level, cbd_level, cbn_level, thc_level_type,
                 cbd_level_type, cbn_level_type, prices, urls, images,
                 description, created_at, updated_at):
        self.id = id
        self.name = name
        self.dispensary_id = dispensary_id
        self.dispensary_valuename = dispensary_name
        self.canabis_brand = canabis_brand
        self.canabis_strain = canabis_strain
        self.category = category
        self.subcategory = subcategory
        self.thc_level = thc_level
        self.cbd_level = cbd_level
        self.cbn_level = cbn_level
        self.thc_levevaluel_type = thc_level_type
        self.cbd_level_type = cbd_level_type
        self.cbn_level_type = cbn_level_type
        self.prices = prices
        self.urls = urls
        self.images = images
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return "Product: %s" % str(self.name)

    def title_str(self):
        # return "%s %s" % (str(self.name), str(self.units))
        return self.name

    def show_product_details(self):
        print "\n================[ Product ]====================="
        print "id . . . . . . . . . : ", self.id
        print "name . . . . . . . . : ", self.name
        print "dispensary_id . . . . .: ", self.dispensary_id
        print "dispensary_valuename . . . . . . : ", self.dispensary_valuename
        print "canabis_brand . . . . . : ", self.canabis_brand
        print "canabis_strain . . .  . .: ", self.canabis_strain
        print "category . . . . . : ", self.category
        print "subcategory . . .  . .: ", self.subcategory
        print "thc_level . . . . . : ", self.thc_level
        print "cbd_level . . .  . .: ", self.cbd_level
        print "cbn_level . . . . . : ", self.cbn_level
        print "thc_levevaluel_type . . .  . .: ", self.thc_levevaluel_type
        print "cbd_level_type . . . . . : ", self.cbd_level_type
        print "cbn_level_type . . .  . .: ", self.cbn_level_type
        print "prices . . .  . .: "
        for price in self.prices:
            print "  ", price
        print "urls . . .  . .: ",
        for url in self.urls:
            print "    ", url
        print "images . . .  . .: "
        for image in self.images:
            print "  ", image
        print "description . . .  . .: ", self.description
        print "created_at . . .  . .: ", self.created_at
        print "updated_at . . .  . .: ", self.updated_at
        print "================================================\n"

    def get_price(self):
        return self.prices[0]

class UrlInfo:
    def __init__(self, admin, public):
        self.admin = admin
        self.public = public

    def __str__(self):
        return "UrlInfo: admin=%s, public=%s" % (str(self.admin),
                                                 str(self.public))


class Price:
    def __init__(self, cost, value):
        self.cost = cost
        self.value = value

    def __str__(self):
        return "Price: %s" % str(self.value)


class Image:
    def __init__(self, main, url):
        self.main = main
        self.url = url

    def __str__(self):
        return "Image: %s" % str(self.url)


if __name__ == "__main__":
    print Image(True, "http://some-path/a.jpg")
