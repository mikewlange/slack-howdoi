# -*- coding: utf-8 -*-
import os

from bottle import get, post, request, run, hook, template, route
import subprocess

from howdoi import howdoi
import sys
# Test this command in a dos window if you are having trouble.
HOW_DO_I_COMMAND =  'python -m howdoi.howdoi'


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
    QueryHowDoI(query)
   

def QueryHowDoI():
    '''
    Kicks off a subprocess to send the 'Query' to HowDoI
    Prints the result, which in this program will route to a gooeyGUI window
    :param Query: text english question to ask the HowDoI web engine
    :return: nothing
    '''
    
    Query = "Rreverse a string in python"
    howdoi_command = HOW_DO_I_COMMAND
    full_text_option = ' -a' 
    t = subprocess.Popen(howdoi_command + ' \"'+ Query + '\" -n ' + str(1)+full_text_option, stdout=subprocess.PIPE)
    (output, err) = t.communicate()
    print('{:^88}'.format(Query.rstrip()))
    print('_'*60)
    print(output.decode("utf-8") )
    return template(output.decode("utf-8") )
    exit_code = t.wait()
    
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', False)
    run(host='0.0.0.0', port=port, debug=debug)
