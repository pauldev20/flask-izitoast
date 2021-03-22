from jinja2 import Markup, Template
from flask_assets import Environment, Bundle
from flask import current_app, render_template, get_flashed_messages
import os


class _izi(object):
    @staticmethod
    def message():
        izi_options = '''
        iziToast.settings({
            timeout: %s
        });''' % (
            current_app.config.get('IZI_TIMEOUT')
        )
        tmp = '''
{% with messages = get_flashed_messages(with_categories=true) %}
{% if messages %}
<script>
document.addEventListener("DOMContentLoaded", function(){
    {{ izi_options }}
    {% for category, message in messages %}
    {% if category is undefined or category == 'message' %}
        iziToast.info({
            title: \'{{ category|capitalize }}\',
            message: \'{{ message }}\',
            # position: \''''+current_app.config.get('IZI_POSITION')+'''\'
        });
    {% else %}
        iziToast.{{ category }}({
            title: \'{{ category|capitalize }}\',
            message: \'{{ message }}\',
            position: \''''+current_app.config.get('IZI_POSITION')+'''\'
        });
    {% endif %}
    {% endfor %}
});
</script>
{% endif %}
{% endwith %}
'''
        message = Template(tmp)
        return Markup(render_template(
          message,
          get_flashed_messages=get_flashed_messages,
          izi_options=izi_options)
          )


class Izi(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['izi'] = _izi
        app.context_processor(self.context_processor) 

        assets = Environment(app)

        module_folder = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
        asset_folder = f'{module_folder}/assets/'

        js = Bundle(f'{asset_folder}js/iziToast.js', output='izi/js.js')
        css = Bundle(f'{asset_folder}css/iziToast.css', output='css/css.css')
        assets.register('izi_js', js)
        assets.register('izi_css', css)

        app.config.setdefault('IZI_TIMEOUT', 15000)
        app.config.setdefault('IZI_POSITION', 'bottomRight')

    @staticmethod
    def context_processor():
        return {'izi': current_app.extensions['izi']}

    def create(self, timestamp=None):
        return current_app.extensions['izi'](timestamp)