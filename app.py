"""
Eldy Deines - Madlibs Exercise
    Madlibs uses dynamic templates with Jinga and uses static files. 
    We utilize Story Class to generate various properties that correlate to words. 
    This will allow us to be adjust to new properties in the story in the FORM HTML template. 
    Upon submission from Form, user is routed to the story print out. 
"""

from stories import story  #Class helps to generate story
from flask import Flask, request, render_template #imports flask object, request, and jinga
from flask_debugtoolbar import DebugToolbarExtension #helps with debugging with html templates

#creates new app and you must provide key right after
app = Flask(__name__)
app.config['SECRET_KEY'] = "CBsecret"

#this associates a new debugger with the app
debug = DebugToolbarExtension(app)

#uses story to generate words on the form, which then gets information from user to build story
@app.route('/form')
def madlib_form():
    prompts = story.prompts
    return render_template("form.html",prompts=prompts)

#use generate function to create story with the form arguments and then publishes to madlib html
@app.route('/story')
def madlib_story():
    user_story = story.generate(request.args)
    return render_template("madlib.html", user_story = user_story)