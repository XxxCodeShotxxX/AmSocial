import os
from Application import App as app




app.run(port=app.config['PORT'],
        debug=app.config['DEBUG'])