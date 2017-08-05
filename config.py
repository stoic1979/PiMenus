import ConfigParser


class Config:

    def __init__(self):
        self.parser = ConfigParser.ConfigParser()
        self.parser.read("settings.ini")

    def set_data(self, theme, gfont, fsize, fcolor, scrollrate, upmenu):
        parser = ConfigParser.ConfigParser()
        parser.read("settings.ini")

        print "Sections: ", parser.sections()

        # print "Menus:", parser.options('Menus')

        parser.set('Menus', 'theme', theme)
        parser.set('Menus', 'google_font', gfont)
        parser.set('Menus', 'font_size', fsize)
        parser.set('Menus', 'font_color', fcolor)
        parser.set('Menus', 'scroll_rate', scrollrate)
        parser.set('Menus', 'update_menu', upmenu)

        # Writing our configuration file to 'settings.ini'
        # with open('settings.ini', 'wb') as configfile:
        with open('settings.ini', 'w') as configfile:
            parser.write(configfile)

    def get(self):
        item = {}
        item['theme'] = self.parser.get('Menus', 'theme')
        item['google_font'] = self.parser.get('Menus', 'google_font')
        item['font_size'] = self.parser.get('Menus', 'font_size')
        item['font_color'] = self.parser.get('Menus', 'font_color')
        item['scroll_rate'] = self.parser.get('Menus', 'scroll_rate')
        item['update_menu'] = self.parser.get('Menus', 'update_menu')
        return item

    def get_theme(self):
        return self.parser.get('Menus', 'theme')

    def get_google_font(self):
        return self.parser.get('Menus', 'google_font')

    def get_font_size(self):
        return self.parser.get('Menus', 'font_size')

    def get_font_color(self):
        return self.parser.get('Menus', 'font_color')

    def get_scroll_rate(self):
        return self.parser.get('Menus', 'scroll_rate')

    def get_update_menu(self):
        return self.parser.get('Menus', 'update_menu')

if __name__ == '__main__':
    config = Config()
    config.get_theme()
