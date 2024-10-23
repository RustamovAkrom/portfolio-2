from flask import request
from app.models import Social


def socials():
    return Social.query.all()


def is_hx_request():
    return request.headers.get("HX-Request") is not None


def setup_context_processor(app):
    @app.context_processor
    def inject_global_functions():
        return dict(
            socials=socials,
            is_htmx=is_hx_request,
        )
