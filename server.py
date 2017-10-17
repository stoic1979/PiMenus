from flask import Flask, redirect, render_template, request, url_for
import traceback
from parser import Parser
from api_manager import ApiManager
from utils import read_logs, flog, uptime
from config import Config
import os
from data import get_vapes, get_syringes, get_accessories, get_concentrates, \
    get_other, get_cat,  get_satvia_second, \
    get_sativa_flower, get_sativa, get_indica

app = Flask(__name__)
parser = Parser('test_xml.xml')


@app.route('/system_update', methods=['POST'])
def system_update():
    try:
        flog("SYSTEM UPDATE")
        key = request.form['key']

        am = ApiManager(key)
        token = am.get_token()
        xml = am.get_products_by_dispensary(token, '684')

        # write xml string in latest.xml
        f = open('latest.xml', 'w')
        f.write('%s' % xml)
        f.close()

    except Exception as exp:
        print('system_update() :: Got exp: %s' % exp)
        flog('system update failed')
    return 'api key: % s' % key


@app.route('/system')
def system():
    time = uptime()
    template_data = {'title': 'System', 'time': time}
    return render_template("system.html", **template_data)


@app.route('/menus')
def menus():
    config = Config()
    themes = ['Prerolls', 'Premium', 'Extracts']
    google_fonts = ['Arial', 'Arial Narrow']
    update_menu = ['1 mins', '2 mins', '5 mins', '10 mins']
    cur_themes = config.get_theme()
    cur_google_fonts = config.get_google_font()
    cur_update_menu = config.get_update_menu()

    templateData = {'title': 'Menu',
                    'font_size': config.get_font_size(),
                    'font_color': config.get_font_color(),
                    'scroll_rate': config.get_scroll_rate(),
                    'themes': themes,
                    'google_fonts': google_fonts,
                    'update_menu': update_menu,
                    'cur_themes': cur_themes,
                    'cur_google_fonts': cur_google_fonts,
                    'cur_update_menu': cur_update_menu}
    return render_template("menus.html", **templateData)


@app.route('/save', methods=['POST'])
def save():
    config = Config()
    try:
        theme = request.form['theme']
        gfont = request.form['gfont']
        fsize = request.form['fsize']
        fcolor = request.form['fcolor']
        scrollrate = request.form['scrollrate']
        upmenu = request.form['upmenu']
        config.set_data(theme, gfont, fsize, fcolor, scrollrate, upmenu)
    except Exception as exp:
        print('save() :: Got exception: %s' % exp)
        print(traceback.format_exc())
        return "Got exception in saving menu: %s" % exp
    templateData = {'title': 'Menu Save'}
    return render_template("menus_save.html", **templateData)


@app.route('/')
def home():
    config = Config()
    try:
        if config.get_theme() == 'Prerolls':
            templateData = {'title': 'Home Page', 'first': get_sativa(),
                            'indica': get_indica(),
                            'second': get_satvia_second()}
            return render_template("prerolls.html", **templateData)

        if config.get_theme() == 'Premium':
            templateData = {'title': 'Home Page', 'sativa': get_sativa()}
            return render_template("flower.html", **templateData)

        if config.get_theme() == 'Extracts':
            vapes = []

            templateData = {'title': 'Home Page', 'vapes': get_vapes(),
                            'syringes': get_syringes(),
                            'accessories': get_accessories(),
                            'concentrates': get_concentrates(),
                            'other': get_other(),
                            'cat': get_cat()}
            return render_template("extracts.html", **templateData)
    except Exception as exp:
        print('home() :: Got exception: %s ' % exp)
        print(traceback.format_exc())


@app.route('/inventory')
def inventory():
    # data = parser.get_all_data()
    # for d in data:
    #     print '', d.id
    #     print '', d.name
    #     # print '', d.category.xml
    #     for cat in d.category:
    #         print '', cat.id
    #         print '', cat.name
    # templateData = {'title': 'Inventory', "all_data": data}
    templateData = {'title': 'Inventory'}
    return render_template("inventory.html", **templateData)


@app.route('/log')
def log():
    templateData = {'title': 'Log', 'logs': read_logs()}
    return render_template("log.html", **templateData)


###################################
#   Prerolls, Extracts, premium   #
###################################
@app.route("/prerolls")
def prerolls():
    for data in get_sativa():
            print "++++++++++++++++++++++++++++", data
    templateData = {'title': 'Home Page', 'first': get_sativa(), 'indica': get_indica(),
                    'second': get_satvia_second()}
    return render_template("prerolls.html", **templateData)


@app.route("/extracts")
def extracts():

    vapes = []
    for s in get_vapes():
        print "", s

    templateData = {'title': 'Home Page',
                    'vapes': get_vapes(),
                    'syringes': get_syringes(),
                    'accessories': get_accessories(),
                    'concentrates': get_concentrates(),
                    'other': get_other(),
                    'cat': get_cat()}
    return render_template("extracts.html", **templateData)


##################################
#           orignal              #
##################################
@app.route("/premium")
def premium():
    # print "++++++++++++++++++++++++++++++++++++++++"

    print "", get_sativa()
    print "++++++++++++++++++++++++++++++++++++++++", get_sativa()

    # templateData = {'title': 'Home Page', 'sativa': get_sativa_flower()}
    templateData = {'title': 'Home Page', 'sativa': get_sativa()}
    return render_template("flower.html", **templateData)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)
