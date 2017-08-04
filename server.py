from flask import Flask, render_template, request
import traceback
from parser import Parser
from api_manager import ApiManager
from utils import read_logs, flog
# from data import get_vapes, get_syringes, get_accessories, get_concentrates, \
#    get_other, get_cat, get_satvia_first, get_satvia_second


app = Flask(__name__)
parser = Parser('test_xml.xml')


@app.route("/menu")
def menu():
    templateData = {'title': 'Menu', 'logs': read_logs()}
    return render_template("menu.html", **templateData)


@app.route('/system_update', methods=['POST'])
def system_update():
    try:
        flog("SYSTEM UPDATE")
        print '======================', request.form
        key = request.form['key']

        am = ApiManager(key)
        token = am.get_token()
        xml = am.get_products_xml(token, 10)

        # write xml string in latest.xml
        f = open('latest.xml', 'w')
        f.write('%s' % xml)
        f.close()

    except Exception as exp:
        print('system_update() :: Got exp: %s' % exp)
    return 'api key: % s' % key


@app.route('/save', methods=['POST'])
def save():
    try:
        theme = request.form['theme']
        gfont = request.form['gfont']
        fsize = request.form['fsize']
        fcolor = request.form['fcolor']
        scrollrate = request.form['scrollrate']
        upmenu = request.form['upmenu']
    except Exception as exp:
        print('save() :: Got exception: %s' % exp)
        print(traceback.format_exc())
    return 'save'


@app.route('/system')
def system():
    templateData = {'title': 'System'}
    return render_template("system.html", **templateData)


@app.route('/menus')
def menus():
    templateData = {'title': 'Menu'}
    return render_template("menus.html", **templateData)


@app.route('/inventory')
def inventory():
    data = parser.get_all_data()
    for d in data:
        print '', d.id
        print '', d.name
        # print '', d.category
        for cat in d.category:
            print '', cat.id
            print '', cat.name
    templateData = {'title': 'Inventory', "all_data": data}
    return render_template("inventory.html", **templateData)


@app.route('/log')
def log():
    templateData = {'title': 'Log', 'logs': read_logs()}
    return render_template("log.html", **templateData)

if __name__ == '__main__':
    app.run(debug=True, '0.0.0.0', port=5000, threaded=True)
