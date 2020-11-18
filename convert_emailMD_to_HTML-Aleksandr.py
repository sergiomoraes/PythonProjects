import os
from datetime import datetime
from random import choice
from jinja2 import Template
from markdown2 import markdown
from subprocess import Popen, PIPE
from helpers import exception_handler

class CreateHtml:
    def __init__(self, markdown_path='./markdown_pad.md'):
        self.PATH_MARKDOWN = os.path.realpath(markdown_path)
        self.PATH_TEMPLATE = os.path.realpath('./template.mjml')
        self.PATH_MJML = os.path.realpath('./node_modules/mjml/bin/mjml')
        self.PATH_EXPORT_HTML = self.get_html_export_path()
        self.PATH_EXPORT_MJML = self.get_mjml_export_path()
    
    def __call__(self):
        t = self.get_template()
        raw_html = self.get_markdown()
        
        html = t.render(content=raw_html)
        
        with open(self.PATH_EXPORT_HTML, 'w') as _f:
            _f.write(html)
            _f.close()
        return self.render_mjml()
    def get_html_export_path(self):
        path = os.path.realpath('./renders/rendered_{dt}.html'.format(
            dt=datetime.strftime(datetime.now(), '%Y%m%d')
        ))
        if os.path.isfile(path):
            file_cnt = 1
            while os.path.isfile(path.replace('.html', '_{c}.html'.format(c=file_cnt))):
                file_cnt += 1
            path = path.replace('.html', '_{c}.html'.format(c=file_cnt))
        return path
    def get_mjml_export_path(self):
        path = os.path.realpath('./renders/rendered_mjml_{dt}.html'.format(
            dt=datetime.strftime(datetime.now(), '%Y%m%d')
        ))
        if os.path.isfile(path):
            file_cnt = 1
            while os.path.isfile(path.replace('.html', '_{c}.html'.format(c=file_cnt))):
                file_cnt += 1
            path = path.replace('.html', '_{c}.html'.format(c=file_cnt))
        return path
    def get_template(self, template_path=None):
        try:
            if not template_path:
                template_path=self.PATH_TEMPLATE
            if not os.path.isfile(template_path):
                raise FileNotFoundError('Template not found at %s' % template_path)
            _html = ''
            with open(template_path, 'r') as _f:
                _html = _f.read()
                _f.close()
            if not _html:
                raise ValueError('html template is empty')
            return Template(_html)
        except Exception as _err:
            exception_handler('get_template', _err)
    def get_markdown(self, markdown_path=None):
        if not markdown_path:
            markdown_path=self.PATH_MARKDOWN
        with open(markdown_path, 'r') as _f:
            raw = _f.read()
            _f.close()
        return markdown(raw)
    def render_mjml(self):
        terminal = Popen(
            'node {c} {ip} -o {ep}'.format(
                c=self.PATH_MJML,
                ip=self.PATH_EXPORT_HTML,
                ep=self.PATH_EXPORT_MJML
            ),
            shell=True, 
            stderr=PIPE,
            stdout=PIPE
        )
        err = terminal.stderr.read().decode('utf8')
        if err:
            raise ValueError(err)
        
        msg = terminal.stdout.read().decode('utf8')
        if msg:
            print('mjml render msg: %s' % msg)
        return {
            'path': self.PATH_EXPORT_MJML,
            'msg': msg
        }

if __name__ == '__main__':
    CreateHtml()()