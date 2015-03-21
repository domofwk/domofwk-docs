from fabric.api import local

def html():
    local('hovercraft -t ./sixfeetup_hovercraft  formation_flask.rst ./build/')
