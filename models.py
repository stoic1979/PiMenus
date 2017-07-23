class Meta_Data:
    def __init__(self, total, count, per_page,
                 current_page, total_pages, links):
        self.total = total
        self.count = count
        self.per_page = per_page
        self.current_page = current_page
        self.total_pages = total_pages
        self.links = links

    def show_meta_details(self):
        print "\n================[ Meta Data ]=================="
        print "total . . . . . .: ", self.total
        print "count . . . . . .: ", self.count
        print "per_page . . . . : ", self.per_page
        print "current_page . . : ", self.current_page
        print "total_pages. . . : ", self.total_pages
        print "links . . . . . .: "
        for link in self.links:
            print "   ", link
        print "================================================\n"


class Links:
    def __init__(self, next):
        self.nxt = next

    def __str__(self):
        return "Links next = %s" % str(self.nxt)

    def show_links_details(self):
        print "\n================[ UrlInfo ]====================="
        print "next . . : ", self.nxt
        print "==============================================\n"


class Data:
    def __init__(self, id, name, description, category, units, images,
                 updated_at, created_at, logo):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        #print "[DATA] categoty: ", category
        self.units = units
        self.images = images
        self.updated_at = updated_at
        self.created_at = created_at
        self.logo = logo

    def title_str(self):
        # return "%s %s" % (str(self.name), str(self.units))
        return self.name

    def __str__(self):
        return "Product: %s, category: %s" % \
               (str(self.name), str(self.category))

    def show_data_details(self):
        print "\n================[ Data ]====================="
        print "id . . . . . . . . . : ", self.id
        print "name . . . . . . . . : ", self.name
        print "description . . . . .: ", self.description
        print "category . . . . . . : "
        for categories in self.category:

            print " ", categories
        print "units . . . . . .. . : "
        for unit in self.units:
            print "  ", unit
        print "images . . . . . . . : "
        for image in self.images:
            print "   ", image
        print "updated_at . . . . . : ", self.updated_at
        print "created_at . . .  . .: ", self.created_at
        print "logo . . . . . . . . : "
        for log in self.logo:
            print "   ", log
        print "================================================\n"

class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "Category id=%s, name=%s" % (str(self.id),
                                            str(self.name))

    def show_url_info_details(self):
        print "\n================[ Category ]====================="
        print "id . . : ", self.id
        print "name . : ", self.name
        print "==============================================\n"


class Unit:
    def __init__(self, id, name, key, value):
        self.id = id
        self.name = name
        self.key = key
        self.value = value

    def __str__(self):
        return "Units: %s, %s, %s, %s" % (str(self.id), str(self.name),
                                       str(self.key), str(self.value))

    def show_units_details(self):
        print "\n================[ Unit ]====================="
        print "cost . .: ", self.cost
        print "value . : ", self.value
        print "==============================================\n"


class Image:
    def __init__(self, id, name, thumb, aspectRatio, listing_medium,
                 listing_small, listing_large, square_medium, square_small,
                 square_large):
        self.id = id
        self.name = name
        self.thumb = thumb
        self.aspectRatio = aspectRatio
        self.listing_medium = listing_medium
        self.listing_small = listing_small
        self.listing_large = listing_large
        self.square_medium = square_medium
        self.square_small = square_small
        self.square_large = square_large

    def __str__(self):
        return "id: %s , name : %s, thumb : %s, aspectRatio : %s, " \
               "listing_medium : %s, listing_small : %s, " \
               "listing_large : %s, " \
               "square_medium : %s, square_small : %s, " \
               "square_large : %s" % (str(self.id), str(self.name),
                                      str(self.thumb),
                                      str(self.aspectRatio),
                                      str(self.listing_medium),
                                      str(self.listing_small),
                                      str(self.listing_large),
                                      str(self.square_medium),
                                      str(self.square_small),
                                      str(self.square_large))

    def show_image_details(self):
        print "\n================[ Image ]===================="
        print "main . : ", self.main
        print "url . .: ", self.url
        print "==============================================\n"


class Logo:

    def __init__(self, id, name, thumb, aspectRatio, listing_medium,
                 listing_small, listing_large, square_medium, square_small,
                 square_large):
        self.id = id
        self.name = name
        self.thumb = thumb
        self.aspectRatio = aspectRatio
        self.listing_medium = listing_medium
        self.listing_small = listing_small
        self.listing_large = listing_large
        self.square_medium = square_medium
        self.square_small = square_small
        self.square_large = square_large

    def __str__(self):
        return "id: %s , name : %s, thumb : %s, aspectRatio : %s, " \
               "listing_medium : %s, listing_small : %s, " \
               "listing_large : %s, " \
               "square_medium : %s, square_small : %s, " \
               "square_large : %s" % (str(self.id), str(self.name),
                                      str(self.thumb),
                                      str(self.aspectRatio),
                                      str(self.listing_medium),
                                      str(self.listing_small),
                                      str(self.listing_large),
                                      str(self.square_medium),
                                      str(self.square_small),
                                      str(self.square_large))
