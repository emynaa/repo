
from unittest import result
from django.shortcuts import render
from . import *
import subprocess
from subprocess import *
from sys import stdout, stdin, stderr




def vm(request):
    return render(request, 'index.html')


def myform(request):
    return render(request, 'myform.html')

def function(request):
    result= subprocess.run('ansible-playbook','play.yml' ,stdin=subprocess.PIPE,shell=True,stdout=subprocess.PIPE)
    
    out, err = result.communicate()
    return render (request , 'index.html')





