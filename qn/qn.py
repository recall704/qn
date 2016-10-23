#coding: utf-8

import os, sys
import getopt
import optparse

import ConfigParser

from sevencow import Cow

conf = ConfigParser.ConfigParser()
current_path = os.path.abspath(os.path.dirname(__file__))
conf_file = os.path.join(current_path, 'qiniu.conf')


def init_qiniu(ak, sk, bk, host_name):
    if not conf.has_section('qiniu'):
        conf.add_section('qiniu')
    conf.set('qiniu', 'ak', ak)
    conf.set('qiniu', 'sk', sk)
    conf.set('qiniu', 'bk', bk)
    conf.set('qiniu', 'host_name', host_name)
    
    conf.write(open(conf_file, 'w'))


def put_file_to_qiniu(file_path):
    conf.read(conf_file)
    access_key = conf.get("qiniu", 'ak')
    secret_key = conf.get("qiniu", 'sk')
    bucket_name = conf.get("qiniu", 'bk')
    host_name = conf.get("qiniu", 'host_name')

    cow = Cow(access_key, secret_key)
    b = cow.get_bucket(bucket_name)
    result = b.put(file_path)
    file_name = result.get('key')
    result = '\n\t![]({host_name}{file_name})\n'.format(host_name=host_name, file_name=file_name)
    print result
    return result


def help():
    help_string =  """
    Usage:

        qiniu init --ak="your_access_key" --sk="your_secret_key" --bk="your_bucket_name" --host_name="your_host_name"

        qiniu put file_path
    """
    print help_string


def main():
    parser = optparse.OptionParser()
    parser.add_option(
        "-a",
        "--ak",
        dest="ak",
        help="access_key"
    )
    parser.add_option(
        "-s",
        "--sk",
        dest="sk",
        help="secret_key"
    )
    parser.add_option(
        "-b",
        "--bk",
        dest="bk",
        help="bucket_name"
    )
    parser.add_option(
        "-n",
        "--host_name",
        dest="host_name",
        help="host_name"
    )
    
    options, args = parser.parse_args(sys.argv[1:])

    if len(args) == 0:
        help()
        return

    action = args[0]
    if action.strip() == 'init':
        ak = options.ak
        sk = options.sk
        bk = options.bk
        host_name = options.host_name

        init_qiniu(ak=ak, sk=sk, bk=bk, host_name=host_name)
    elif action.strip() == 'put':
        file_path = args[1]
        put_file_to_qiniu(file_path)
    else:
        help()

if __name__ == '__main__':
    main()
