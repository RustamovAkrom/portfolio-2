from functools import wraps

from flask import render_template, request


def htmx_route():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            context = func(**kwargs)

            template_htmx = context['template_name']

            if not request.headers.get("HX-Request"):
                context['template_htmx'] = template_htmx
                template_name = "include_content.html"

                return render_template(template_name, **context)
            return render_template(template_htmx, **context)
        return wrapper
    return decorator
