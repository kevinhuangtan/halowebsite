from flask import Flask, render_template, request
import os
from halotools.halotools.empirical_models import hod_components
from halotools.halotools.empirical_models import halo_prof_components
from halotools.halotools.empirical_models import gal_prof_factory

application = Flask(__name__)

Zheng = hod_components.Zheng07Cens.__init__.__doc__

Isotropic = gal_prof_factory.IsotropicGalProf.__init__.__doc__


@application.route("/", methods=['GET', 'POST'])
def hello():
    if (request.method == 'POST'):
        print 'post'
        print request.json
        print request.data
        os.system('sudo rm -r -f halotools')
        os.system('git clone https://github.com/astropy/halotools.git')
        path = 'halotools'
        filename = '__init__.py'
        open(os.path.join(path,filename),'w')
        os.system('sudo reload halo')
        return "<h1 style='color:blue'>Edited</h1>"        
    else:
        print 'normal request'
        return render_template('test.html', Zheng = Zheng, Isotropic = Isotropic)


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
    application.run(host='0.0.0.0')

