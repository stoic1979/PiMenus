from products_parser import *

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


def get_vapes():
    return get_products_by_category('extracts', 'vapes')


def get_syringes():
    return get_products_by_category('extracts', 'syringes')


def get_accessories():
    return get_products_by_category('extracts', 'accessories')


def get_concentrates():
    return get_products_by_category('extracts', 'concentrates')


def get_other():
    return get_products_by_category('extracts', 'other')


def get_cat():
    return get_products_by_category('extracts', 'cat 4')


def get_satvia_first():
    return [
        Item('BAM Rosin Rockets: Blue Gorilla', '$14'),
        Item('BAM Rosin Rockets: Forum Sin Mint Cookies', '$14'),
        Item('BAM Rosin Rockets: Key Lime Gorilla', '$14'),
        Item('BAM Rosin Rockets: Sin Mint Cookies', '$14'),
        Item('BAM Rosin Rockets: White Nightmare', '$14'),
        Item('BAM Rosin Rockets: White Strawberry', '$14'),
        Item('BAM Rosin Rockets: Bubba Cookies', '$14'),
        Item('BAM Rosin Rockets: Body & Mind', '$14'),
    ]


def get_satvia_second():
    return [
        Item('Matrix 3PK Cones', '$14'),
        Item('Willie Nelson Reserve', '$14'),
        Item('GLP Green Life Productions Prerolls', '$14'),
        Item('Cannabiotix', '$14'),
        Item('SST Californias Finest', '$14'),
        Item('PW Killa Collection', '$14'),
        Item('BAM Rosin Rockets: Key Lime Strawberry', '$14'),
        Item('BAM Rosin Rockets: Blue Cookies', '$14'),
    ]


def get_satvia_other():
    return [
        Item('BAM Rosin Rockets: Blue Gorilla', '$14'),
        Item('BAM Rosin Rockets: Forum Sin Mint Cookies', '$14'),
        Item('BAM Rosin Rockets: Key Lime Gorilla', '$14'),
    ]
