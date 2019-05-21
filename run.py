# Run a test server.
from app import create_app

app = create_app(config_filename='..\config.py')
app.run(host='0.0.0.0', debug=app.config['DEBUG'])
