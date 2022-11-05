#
#
#

from urllib.parse import urljoin, urlparse

from flask import request, session, url_for
from flask import redirect as redirect_unsafe

#
#
#
def is_safe_url(target):
    url_ref = urlparse(request.host_url)
    url_audit = urlparse(urljoin(request.host_url, target))
    return url_audit.scheme in ('http', 'https') and url_ref.netloc == url_audit.netloc

#
#
#
def redirect(endpoint, **values):
    target = None
    if 'next' in session:
        target = session['next']
    if not target or not is_safe_url(target):
        target = url_for(endpoint, **values)
    return redirect_unsafe(target)
