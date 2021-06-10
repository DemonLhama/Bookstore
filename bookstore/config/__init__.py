def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///bookstore.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = 'somethinghard159'
    app.config['JWT_SECRET_KEY'] = 'somethinghardagain123'
    app.config['JWT_BLACKLIST_ENABLE'] = True
    