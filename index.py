#!/usr/bin/env python
# encoding: utf-8
"""
index.py

Created by Maksim Tsvetovat on 2013-11-09.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""
from flask import Flask, render_template, request, abort, g, json, session, redirect

import requests

from app import app, db
from imagesearch import get_image


import pudb

@app.route("/")
def index():
    return(render_template("main.html"))
    
    
@app.route("/search/", methods=['GET', 'POST'])
def search():
    terms = request.form.get('search')
    companies = list(db.ca.find({'company_name':terms}))
    companies = db.command('text', 'ca', search=terms)['results']
    
    for company in companies:
        company.update(company['obj'])
        epa_results = db.command('text','epa', search=company['company_name'])
        company['epa_citations'] = epa_results['stats']['nscanned']
        company['epa_rating'] = (float(company['epa_citations'])/1000)
        print company['epa_citations'], company['epa_rating']
    
    return(render_template("results.html", companies = companies, get_image=get_image))