#
# script for parsing products' xml
# and creating data models to be used by ui
#
import xml.etree.ElementTree as ET
from models import Pagination, Product, Price, UrlInfo, Image


class ProductParser:

    def __init__(self, file_path):
        self.file_path = file_path
        tree = ET.parse(file_path)
        self.root = tree.getroot()

        for child in self.root:
            if child.tag == 'products':
                self.products = child

            if child.tag == 'pagination':
                self.pagination = child

    def get_pagination(self):
        """
        function parser the pagination xml file
        """

        print "getting pagination"

        current_page = self.pagination.find('current_page').text
        last_page = self.pagination.find('last_page').text
        per_page = self.pagination.find('per_page').text
        has_more_pages = self.pagination.find('has_more_pages').text
        first_item = self.pagination.find('first_item').text
        last_item = self.pagination.find('last_item').text
        total = self.pagination.find('total').text
        count = self.pagination.find('count').text

        return Pagination(current_page, last_page, per_page,
                          has_more_pages, first_item,
                          last_item, total, count)

    def get_products(self):
        """
        function parses the products xml file
        and returns list of products
        """

        lst = []
        for product in self.products.findall('product'):
            id = product.find('id').text
            name = product.find('name').text
            dispensary_id = product.find('dispensary_id').text
            dispensary_name = product.find('dispensary_name').text
            canabis_brand = product.find('canabis_brand').text
            canabis_strain = product.find('canabis_strain').text
            category = product.find('category').text
            subcategory = product.find('subcategory').text
            thc_level = product.find('thc_level').text
            cbd_level = product.find('cbd_level').text
            cbn_level = product.find('cbn_level').text
            thc_level_type = product.find('thc_level_type').text
            cbd_level_type = product.find('cbd_level_type').text
            cbn_level_type = product.find('cbn_level_type').text

            description = product.find('description').text
            created_at = product.find('created_at').text
            updated_at = product.find('updated_at').text

            prices = []
            urls = []
            images = []

            for child in product:
                if child.tag == 'prices':
                    for cost in child.findall('cost'):
                        prices.append(Price(cost.attrib['unit'], cost.text))

                if child.tag == 'urls':
                    admin = child.find('admin').text
                    public = child.find('public').text
                    urls.append(UrlInfo(admin, public))

                if child.tag == 'images':
                    for image in child.findall('image'):
                        images.append(Image(image.attrib['main'], image.text,))

            lst.append(Product(id, name, dispensary_id, dispensary_name,
                               canabis_brand, canabis_strain,
                               category, subcategory, thc_level, cbd_level,
                               cbn_level, thc_level_type, cbd_level_type,
                               cbn_level_type, prices, urls, images,
                               description, created_at, updated_at))

        return lst


def get_products_by_category(category, subcategory):
    pp = ProductParser('products.xml')

    return [product for product in pp.get_products() if product.category == category and product.subcategory == subcategory]



def get_all_products():
    pp = ProductParser('products.xml')

    return pp.get_products()


def get_first_data():
    return ['BAM Rosin Rockets: Blue Gorilla',
            'BAM Rosin Rockets: Forum Sin Mint Cookies',
            'BAM Rosin Rockets: Key Lime Gorilla',
            'BAM Rosin Rockets: Sin Mint Cookies',
            'BAM Rosin Rockets: White Nightmare',
            'BAM Rosin Rockets: White Strawberry',
            'BAM Rosin Rockets: Bubba Cookies',
            'BAM Rosin Rockets: Body & Mind']


def get_second_data():
    return ['Matrix 3PK Cones',
            'Whillie Nelson Reserve',
            'GLP Green Life Production prerolls',
            'Cannabiotix',
            'SST Californias Finest',
            'PW Killa Collection',
            'BAM Rosin Rockets: Key Lime Strawberry',
            'BAM Rosin Rockets: Blue Cookies']


def get_other_data():
    return ['BAM Rosin Rockets: Blue Gorilla               $14',
            'BAM Rosin Rockets: Forum Sin Mint Cookies     $14',
            'BAM Rosin Rockets: Key Lime Gorilla           $14']

if __name__ == "__main__":

    print get_products_by_category('PreRolls', 'Satvia')
    print get_products_by_category('PreRolls', 'Hybrid')
    print get_products_by_category('PreRolls', 'Indica')


    """
    pp = ProductParser('products.xml')

    products = pp.get_products()
    for product in products:
        product.show_product_details()

    pagination = pp.get_pagination()
    pagination.show_pagination_details()
    """
