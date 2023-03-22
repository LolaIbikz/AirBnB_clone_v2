#!/usr/bin/python3
""" Script that distributes an archive to your web servers using do_deploy"""

from fabric.api import local
from fabric.operations import run, put, sudo
import os.path
from fabric.api import env
env.hosts = ['35.185.103.0', '35.237.21.105']


def do_deploy(archive_path):
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        nconfig = archive_path.split("/")[-1]
        ndir = ("/data/web_static/releases/" + nconfig.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(ndir))
        run("sudo tar -xzf /tmp/{} -C {}".format(nconfig, ndir))
        run("sudo rm /tmp/{}".format(nconfig))
        run("sudo mv {}/web_static/* {}/".format(ndir, ndir))
        run("sudo rm -rf {}/web_static".format(ndir))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(ndir))
        return True
    except:
        return False
