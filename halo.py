#update when github pull
from flask import Flask, render_template, request
import re
import os
from halotools.halotools.empirical_models import hod_components
from halotools.halotools.empirical_models import halo_prof_components
from halotools.halotools.empirical_models import gal_prof_factory



application = Flask(__name__)



Zheng = [hod_components.Zheng07Cens.__init__.__doc__, 'replace']
Leauthaud = [hod_components.Leauthaud11Sats.__init__.__doc__, 'replace']

Components = [Zheng, Leauthaud]

for j in range(0, len(Components)):
    #probably a more elegant way to do this
    cutRE = re.findall( '----------\n(.*?)Examples', Components[j][0], re.DOTALL)
    param_name = re.findall(r'\w+\s\:', cutRE[0]);
    for i, val in enumerate(param_name):
        param_name[i] = param_name[i][:-2]

    paramters_length = len(param_name)
    
    param_type = re.findall(r':\s.+', cutRE[0]);
    for i, val in enumerate(param_type):
        param_type[i] = param_type[i][2:]

    param_descr = re.findall(r'\n\s\s\s\s\s\s\s\s\s\s\s\s.+\n\n', cutRE[0])
    for i in range(0, paramters_length):
        param_descr[i] = param_descr[i][13:-2]
    
    parameters = []
    for i, val in enumerate(param_name):
        parameters.append({'name': param_name[i], 'type': param_type[i], 'description': param_descr[i]})
    Components[j][1] = parameters

@application.route("/", methods=['GET', 'POST'])
def hello():
    if (request.method == 'POST'):
        print 'post request'
        os.system('sudo rm -r -f halotools')
        os.system('git clone https://github.com/astropy/halotools.git')
        path = 'halotools'
        filename = '__init__.py'
        open(os.path.join(path,filename),'w')
        os.system('sudo reload halo')
        return "<h1 style='color:blue'>Edited</h1>"        
    else:
        print 'normal request'
        # print Zheng[0]
        return render_template('home.html', components = Components)


@application.route("/payload")
def payload_text():
    print 'test payload'
    os.system('sudo rm -r -f halotools')
    os.system('git clone https://github.com/astropy/halotools.git')
    path = 'halotools'
    filename = '__init__.py'
    open(os.path.join(path,filename),'w')
    os.system('sudo reload halo')
    return "<h1 style='color:blue'>Edited</h1>"


if __name__ == "__main__":
    # application.run(host='0.0.0.0')
    application.run(debug=True)

