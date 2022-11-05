#
#
#

from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask

from app import public, user
from app.extensions import celery, csrf_protect, db, flask_static_digest, login_manager, migrate

#
#
#
def create_app():
    app = Flask(__name__.split('.')[0])
    app.config.from_object('app.settings')
    
    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )

    app.jinja_env.trim_blocks=True
    app.jinja_env.lstrip_blocks=True

    register_extensions(app)
    register_blueprints(app)

    login_manager.login_message_category = 'primary'
    login_manager.login_view = 'public.index'

    create_celery(app)

    return app

#
#
#
def register_blueprints(app):
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(user.views.blueprint)
    return None

#
#
#
def register_extensions(app):
    csrf_protect.init_app(app)
    db.init_app(app)
    flask_static_digest.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    return None

#
#
#
def create_celery(app:Flask=None):
    app = app or create_app()
    celery.conf.update(app.config.get('CELERY', {}))

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
