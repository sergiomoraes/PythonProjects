import os
from datetime import datetime
import mailer
from helpers import exception_handler
from create_html import CreateHtml
from dotenv import load_dotenv

load_dotenv('.env')
EXCH_SERVER = os.getenv('EXCH_SERVER')

def send_mail(_to, _from, _subject, _body='', _html=''):
    """Send Tableau Announcement email in Html form
    
    Args:
        _to (str): email address of recipient
        _from (str): email of sender
        _subject (str): email subject
        _body (str, optional): Defaults to None. email body contents (sent as is)
        _html (str, optional): Defaults to None. Html to render in email body (will be rendered as html)
    """
    # try:
    msg = mailer.Message()
    msg.To = _to
    msg.From = _from
    msg.Subject = _subject
    msg.Body = _body
    msg.Html = _html
    
    m = mailer.Mailer(EXCH_SERVER)
    m.send(msg)
    # except Exception as _err:
    #     exception_handler('send_mail', _err)

def main():
    render_response = CreateHtml()().get('path')
    if not render_response:
        raise ValueError('no path received from render')
    html_path = render_response
    send_mail(
        _from=os.getenv('MAIL_FROM'),
        _to=os.getenv('MAIL_TO'),
        _subject='{s} - {d}'.format(
            s=os.getenv('MAIL_SUBJECT'),
            d=datetime.strftime(datetime.now(), '%Y-%m-%d')
        ),
        _html=open(render_response).read()
    )

if __name__ == "__main__":
    main()