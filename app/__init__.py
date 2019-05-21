from flask import Flask


def create_app(config_filename):
    from app.telegram import telegram

    app = Flask(__name__)
    """
    Application Configuration
    """
    # load default configuration
    # app.config.from_object('project.settings')
    app.config.from_pyfile(config_filename)

    """
    Blueprint Registration
    """
    app.register_blueprint(telegram)

    """
    Fire Services 
    """

    return app
