from functools import wraps

from flask import render_template, redirect, url_for, request
from flask_login import current_user


def htmx_route():
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            context = func(*args, **kwargs)

            template_htmx = context['template_name']

            if not request.headers.get("HX-Request"):
                context['template_htmx'] = template_htmx
                template_name = "include_content.html"

                return render_template(template_name, **context)
            return render_template(template_htmx, **context)
        return wrapper
    return decorator


def get_htmx_context(template_name = None) -> tuple[str, dict]:
    context = {}
    template_htmx = template_name

    if not request.headers.get("HX-Request"):
        context['template_htmx'] = template_htmx
        template_name = "include_content.html"

    return template_name, context

