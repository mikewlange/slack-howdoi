# -*- coding: utf-8 -*-
import os

from bottle import get, post, request, run, hook, template, route

from howdoi import howdoi


@hook('before_request')
def strip_path():
    request.environ['PATH_INFO'] = request.environ['PATH_INFO'].rstrip('/')
    
    
@route('/h/<query>')
def h_handler():
    """
    Example:
        /howdoi open file python
    """
    text = query
    # adding default params
    args = {
        'query': text.split(),
        'pos': 1,
        'all': False,
        'link': False,
        'clear_cache': False,
        'version': False,
        'num_answers': 1,
        'color': False,
    }

    output = howdoi.howdoi(args)
    return template(output)
    
@route('/hdi/<query>')
def hdi_handler():
    """
    Example:
        /howdoi open file python
    """
    text = query

    # adding default params
    args = {
        'query': text.split(),
        'pos': 1,
        'all': False,
        'link': False,
        'clear_cache': False,
        'version': False,
        'num_answers': 1,
        'color': False,
    }

    output = howdoi.howdoi(args)
    return output

@post('/howdoi')
def howdoi_handler():
    """
    Example:
        /howdoi open file python
    """
    postdata = request.body.read()
    print postdata
    text = postdata

    # adding default params
    args = {
        'query': text.split(),
        'pos': 1,
        'all': False,
        'link': False,
        'clear_cache': False,
        'version': False,
        'num_answers': 1,
        'color': False,
    }

    output = howdoi.howdoi(args)
    return output


@route('/')
def index():
    return template('index')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', False)
    run(host='0.0.0.0', port=port, debug=debug)
