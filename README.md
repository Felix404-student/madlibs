# Madlibs
Simple Madlibs form/story genetator with Python, Flask, Jinja

<p>In this exercise, you’ll use Flask to make a Madlibs game.</p>
<div class="section" id="about-madlibs">
<h2>About Madlibs</h2>
<a class="reference internal image-reference" href="_images/madlibs.jpg"><img alt="_images/madlibs.jpg" src="https://curric.rithmschool.com/springboard/exercises/flask-madlibs/_images/madlibs.jpg" style="width: 10em;" /></a>
<p>In Madlibs, you’re asked a series of questions, like this:</p>
<pre class="literal-block">
<em>plural_noun</em>: <strong>turnips</strong>
<em>verb</em>: <strong>juggle</strong>
</pre>
<p>Those are then plugged into a story template, like this:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">I</span> <span class="n">love</span> <span class="n">to</span> <span class="p">{</span><span class="n">verb</span><span class="p">}</span> <span class="p">{</span><span class="n">plural_noun</span><span class="p">}</span><span class="o">.</span>
</pre></div>
</div>
<p>To create a story like:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">I</span> <span class="n">love</span> <span class="n">to</span> <span class="n">juggle</span> <span class="n">turnips</span><span class="o">.</span>
</pre></div>
</div>
</div>
<div class="section" id="code">
<h2>Code</h2>
<p>We’ve given you some code to help with the core non-Flask-specific Madlibs
part:</p>
<div class="literal-block-wrapper docutils container" id="id1">
<div class="code-block-caption"><span class="caption-text">stories.py</span></div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="sd">&quot;&quot;&quot;Madlibs Stories.&quot;&quot;&quot;</span>


<span class="k">class</span> <span class="nc">Story</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;Madlibs story.</span>

<span class="sd">    To  make a story, pass a list of prompts, and the text</span>
<span class="sd">    of the template.</span>

<span class="sd">        &gt;&gt;&gt; s = Story([&quot;noun&quot;, &quot;verb&quot;],</span>
<span class="sd">        ...     &quot;I love to {verb} a good {noun}.&quot;)</span>

<span class="sd">    To generate text from a story, pass in a dictionary-like thing</span>
<span class="sd">    of {prompt: answer, promp:answer):</span>

<span class="sd">        &gt;&gt;&gt; ans = {&quot;verb&quot;: &quot;eat&quot;, &quot;noun&quot;: &quot;mango&quot;}</span>
<span class="sd">        &gt;&gt;&gt; s.generate(ans)</span>
<span class="sd">        &#39;I love to eat a good mango.&#39;</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">words</span><span class="p">,</span> <span class="n">text</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;Create story with words and template text.&quot;&quot;&quot;</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">prompts</span> <span class="o">=</span> <span class="n">words</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">template</span> <span class="o">=</span> <span class="n">text</span>

    <span class="k">def</span> <span class="nf">generate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">answers</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;Substitute answers into text.&quot;&quot;&quot;</span>

        <span class="n">text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">template</span>

        <span class="k">for</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">val</span><span class="p">)</span> <span class="ow">in</span> <span class="n">answers</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;{&quot;</span> <span class="o">+</span> <span class="n">key</span> <span class="o">+</span> <span class="s2">&quot;}&quot;</span><span class="p">,</span> <span class="n">val</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">text</span>


<span class="c1"># Here&#39;s a story to get you started</span>


<span class="n">story</span> <span class="o">=</span> <span class="n">Story</span><span class="p">(</span>
    <span class="p">[</span><span class="s2">&quot;place&quot;</span><span class="p">,</span> <span class="s2">&quot;noun&quot;</span><span class="p">,</span> <span class="s2">&quot;verb&quot;</span><span class="p">,</span> <span class="s2">&quot;adjective&quot;</span><span class="p">,</span> <span class="s2">&quot;plural_noun&quot;</span><span class="p">],</span>
    <span class="sd">&quot;&quot;&quot;Once upon a time in a long-ago {place}, there lived a</span>
<span class="sd">       large {adjective} {noun}. It loved to {verb} {plural_noun}.&quot;&quot;&quot;</span>
<span class="p">)</span>
</pre></div>
</div>
</div>
<p>This allows you to define Madlibs stories, and it can generate the resulting
story from a set of answers. (It’s also a nice example of a small but useful
class!)</p>
<p>We’ve created a story, <cite>story</cite>, in that file.</p>
<div class="admonition warning">
<p>STOP AND EXPLORE HERE</p>
<p class="last">Before starting to make a Flask app, make sure you understand how this
<cite>Story</cite> class works — go into <em>ipython</em> and try out the <cite>generate</cite>
method on our sample story to get a feel for the text-generating
process for Madlibs.</p>
</div>
</div>
<div class="section" id="challenge">
<h2>Challenge</h2>
<p>Write a Flask app that imports the example story. Add a homepage for the
application that shows a form prompting you for all the words in the story:</p>
<a class="reference internal image-reference" href="_images/questions.png"><img alt="_images/questions.png" src="https://curric.rithmschool.com/springboard/exercises/flask-madlibs/_images/questions.png" style="width: 35%;" /></a>
<p><strong>Don’t hardcode this, though</strong> — you want your form route to be able
to ask for all of the questions required by the story, not for it to
have a hard-coded form of asking these exact questions!</p>
<p>Add a route, <cite>/story</cite>, that shows the resulting story for those answers,
like this:</p>
<a class="reference internal image-reference" href="_images/story.png"><img alt="_images/story.png" src="https://curric.rithmschool.com/springboard/exercises/flask-madlibs/_images/story.png" style="width: 65%;" /></a>
<p>For now, don’t worry about having template inheritance or a <cite>base.html</cite> —
later, in further study, you can refactor this to use template inheritance.</p>
</div>
<div class="section" id="further-study">
<h2>Further Study</h2>
<div class="section" id="use-template-inheritance">
<h3>Use Template Inheritance</h3>
<p>Make a <cite>base.html</cite> template of common parts of your templates (like the
<cite>&lt;html&gt;</cite>, <cite>&lt;body&gt;</cite>, and other common things, and change your templates so
they inherit from this base template.</p>
</div>
<div class="section" id="allow-user-to-pick-story">
<h3>Allow User to Pick Story</h3>
<p>Add a feature where there are several different story templates, rather than
just one.</p>
<p>The homepage should change to a drop-down menu of the story templates.
When the user picks a template, it should go to the page that prompts for the
list of story questions. That should, as before, go to the page that shows
the generated story.</p>
</div>
<div class="section" id="add-css">
<h3>Add CSS</h3>
<p><strong>Still want more?</strong> Add some CSS to your madlibs, storing the CSS file
in a <cite>static/</cite> directory and referencing it properly, so Flask will serve
it up.</p>
</div>
</div>
