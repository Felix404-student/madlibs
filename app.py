from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story


app = Flask(__name__)
app.config['SECRET_KEY'] = "super-Duper-secret"

debug = DebugToolbarExtension(app)

# this determines both the prompts and story text.
# can be changed, but the list elements must match the placeholders
story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun", "building", "food", "person", "toy", "dessert", "place_2"],
    """Once upon a time in long-ago {place}, there lived a
       large {adjective} {noun}.\nIt loved to {verb} {plural_noun}.\n
       The {adjective} {noun} lived in a {building} and every day ate {food} 
       for breakfast.\nIt's best friend, {person}, made a {toy} for their birthday and gave it 
       to the {noun} as a present.\nAfter having some birthday {dessert}, they took the {toy} to 
       the {place_2} to watch the {plural_noun} and play with the {toy} together.\nWhat a great 
       day!"""
)

@app.route('/')
def index():
    """Return homepage."""

    return render_template("index.html", story=story)

@app.route('/story')
def generate_story():
    """Return generated story."""

    answers = {}
    
    for answer in story.prompts:
        answers[answer] = request.args[answer]

    full_story = story.generate(answers)


    return render_template("story.html", full_story=full_story)