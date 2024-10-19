from app.models import Social


def socials():
    return Social.query.all()


def setup_context_processor(app):
    @app.context_processor
    def inject_global_functions():
        return dict(socials=socials)
