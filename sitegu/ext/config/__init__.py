def init_app(app):
    app.config["SECRET_KEY"] = "sabino01"

    if app.debug:
        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True