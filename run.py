import os
from Application import App as app,manager



if __name__ =='__main__':

        app.run(port=app.config['PORT'],
                debug=app.config['DEBUG'])