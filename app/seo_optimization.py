from flask import Flask, render_template, Response
import datetime


def setup_seo_optimization(app: Flask):
    @app.route('/sitemap.xml', methods=['GET'])
    def sitemap():
        pages = []
        ten_days_ago = (datetime.datetime.now() - datetime.timedelta(days=10)).date().isoformat()

        # Собираем все маршруты (URL) сайта
        for rule in app.url_map.iter_rules():
            if "GET" in rule.methods and rule.defaults is not None and len(rule.defaults) >= len(rule.arguments):
                pages.append([rule.rule, ten_days_ago])

        sitemap_xml = render_template('sitemap_template.xml', pages=pages)
        response = Response(sitemap_xml, mimetype='application/xml')
        return response
