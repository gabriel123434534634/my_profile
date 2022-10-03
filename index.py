import pl
from bottle import route, run, template, static_file, request, redirect, response, error
import json, re
from datetime import datetime
import subprocess, os, random
from datetime import timedelta
import time
from os import path
import re, traceback
import requests, os
from threading import Thread

@route("/")
def home():
    return template("index.html")
@route("/static")
def static():
    path = request.
run(host="0.0.0.0", port=8080, debug=True)