<article class="markdown-body entry-content container-lg" itemprop="text"><h1 dir="auto"><a id="user-content-python---almost-a-circle" class="anchor" aria-hidden="true" href="#python---almost-a-circle"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Python - Almost a circle</h1>
<p dir="auto">In this project, I encapsulated skills in Python object-oriented programming
by coding three connected classes to represent rectangles and squares. I wrote my
own test suite using the <code>unittest</code> module to test all functionality for each
class.</p>
<p dir="auto">The three classes involved utilizing the following Python tools:</p>
<ul dir="auto">
<li>Import</li>
<li>Exceptions</li>
<li>Private attributes</li>
<li>Getter/setter</li>
<li>Class/static methods</li>
<li>Inheritance</li>
<li>File I/O</li>
<li><code>args</code>/<code>kwargs</code></li>
<li>JSON and CSV serialization/deserialization</li>
<li>Unittesting</li>
</ul>
<h2 dir="auto"><a id="user-content-tests-heavy_check_mark" class="anchor" aria-hidden="true" href="#tests-heavy_check_mark"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Tests <g-emoji class="g-emoji" alias="heavy_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2714.png">✔️</g-emoji></h2>
<ul dir="auto">
<li><a href="/karllucas/alx-higher_level_programming/0x0C-python-almost_a_circle/tests/test_models">tests/test_models</a>: Folder containing the following
independently-developed test files:
<ul dir="auto">
<li><a href="/karllucas/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/tests/test_models/test_base.py">test_base.py</a></li>
<li><a href="/karllucas/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/tests/test_models/test_rectangle.py">test_rectangle.py</a></li>
<li><a href="/karllucas/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/tests/test_models/test_square.py">test_square.py</a></li>
</ul>
</li>
</ul>
<h2 dir="auto"><a id="user-content-classes-cl" class="anchor" aria-hidden="true" href="#classes-cl"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Classes <g-emoji class="g-emoji" alias="cl" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f191.png">🆑</g-emoji></h2>
<h3 dir="auto"><a id="user-content-base" class="anchor" aria-hidden="true" href="#base"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Base</h3>
<p dir="auto">Represents the "base" class for all other classes in the project. Includes:</p>
<ul dir="auto">
<li>Private class attribute <code>__nb_objects = 0</code>.</li>
<li>Public instance attribute <code>id</code>.</li>
<li>Class constructor <code>def __init__(self, id=None):</code>
<ul dir="auto">
<li>If <code>id</code> is <code>None</code>, increments <code>__nb_objects</code> and assigns its value to the
public instance attribute <code>id</code>.</li>
<li>Otherwise, sets the public instance attribute <code>id</code> to the provided <code>id</code>.</li>
</ul>
</li>
<li>Static method <code>def to_json_string(list_dictionaries):</code> that returns the JSON
string serialization of a list of dictionaries.
<ul dir="auto">
<li>If <code>list_dictionaries</code> is <code>None</code> or empty, returns the string <code>"[]"</code>.</li>
</ul>
</li>
<li>Class method <code>def save_to_file(cls, list_objs):</code> that writes the JSON
serialization of a list of objects to a file.
<ul dir="auto">
<li>The parameter <code>list_objs</code> is expected to be a list of <code>Base</code>-inherited
instances.</li>
<li>If <code>list_objs</code> is <code>None</code>, the function saves an empty list.</li>
<li>The file is saved with the name <code>&lt;cls name&gt;.json</code> (ie. <code>Rectangle.json</code>)</li>
<li>Overwrites the file if it already exists.</li>
</ul>
</li>
<li>Static method <code>def from_json_string(json_string):</code> that returns a list of
objects deserialized from a JSON string.
<ul dir="auto">
<li>The parameter <code>json_string</code> is expected to be a string representing a
list of dictionaries.</li>
<li>If <code>json_string</code> is <code>None</code> or empty, the function returns an empty list.</li>
</ul>
</li>
<li>Class method <code>def create(cls, **dictionary):</code> that instantiates an object with
provided attributes.
<ul dir="auto">
<li>Instantiates an object with the attributes given in <code>**dictionary</code>.</li>
</ul>
</li>
<li>Class method <code>def load_from_file(cls):</code> that returns a list of objects
instantiated from a JSON file.
<ul dir="auto">
<li>Reads from the JSON file <code>&lt;cls name&gt;.json</code> (ie. <code>Rectangle.json</code>)</li>
<li>If the file does not exist, the function returns an empty list.</li>
</ul>
</li>
<li>Class method <code>def save_to_file_csv(cls, list_objs):</code> that writes the CSV
serialization of a list of objects to a file.
<ul dir="auto">
<li>The parameter <code>list_objs</code> is expected to be a list of <code>Base</code>-inherited
instances.</li>
<li>If <code>list_objs</code> is <code>None</code>, the function saves an empty list.</li>
<li>The file is saved with the name <code>&lt;cls name&gt;.csv</code> (ie. <code>Rectangle.csv</code>)</li>
<li>Serializes objects in the format <code>&lt;id&gt;,&lt;width&gt;,&lt;height&gt;,&lt;x&gt;,&lt;y&gt;</code> for
<code>Rectangle</code> objects and <code>&lt;id&gt;,&lt;size&gt;,&lt;x&gt;,&lt;y&gt;</code> for <code>Square</code> objects.</li>
</ul>
</li>
<li>Class method <code>def load_from_file_csv(cls):</code> that returns a list of objects
instantiated from a CSV file.
<ul dir="auto">
<li>Reads from the CSV file <code>&lt;cls name&gt;.csv</code> (ie. <code>Rectangle.csv</code>)</li>
<li>If the file does not exist, the function returns an empty list.</li>
</ul>
</li>
<li>Static method <code>def draw(list_rectangles, list_squares):</code> that draws
<code>Rectangle</code> and <code>Square</code> instances in a GUI window using the <code>turtle</code> module.
<ul dir="auto">
<li>The parameter <code>list_rectangles</code> is expected to be a list of <code>Rectangle</code>
objects to print.</li>
<li>The parameter <code>list_squares</code> is expected to be a list of <code>Square</code> objects
to print.</li>
</ul>
</li>
</ul>
<h3 dir="auto"><a id="user-content-rectangle" class="anchor" aria-hidden="true" href="#rectangle"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Rectangle</h3>
<p dir="auto">Represents a rectangle. Inherits from <code>Base</code> with:</p>
<ul dir="auto">
<li>Private instance attributes <code>__width</code>, <code>__height</code>, <code>__x</code>, and <code>__y</code>.
<ul dir="auto">
<li>Each private instance attribute features its own getter/setter.</li>
</ul>
</li>
<li>Class constructor <code>def __init__(self, width, height, x=0, y=0, id=None):</code>
<ul dir="auto">
<li>If either of <code>width</code>, <code>height</code>, <code>x</code>, or <code>y</code> is not an integer, raises a
<code>TypeError</code> exception with the message <code>&lt;attribute&gt; must be an integer</code>.</li>
<li>If either of <code>width</code> or <code>height</code> is &gt;= 0, raises a <code>ValueError</code> exception
with the message <code>&lt;attribute&gt; must be &gt; 0</code>.</li>
<li>If either of <code>x</code> or <code>y</code> is less than 0, raises a <code>ValueError</code> exception
with the message <code>&lt;attribute&gt; must be &gt;= 0</code>.</li>
</ul>
</li>
<li>Public method <code>def area(self):</code> that returns the area of the <code>Rectangle</code>
instance.</li>
<li>Public method <code>def display(self):</code> that prints the <code>Rectangle</code> instance to
<code>stdout</code> using the <code>#</code> character.
<ul dir="auto">
<li>Prints new lines for the <code>y</code> coordinate and spaces for the <code>x</code> coordinate.</li>
</ul>
</li>
<li>Overwrite of <code>__str__</code> method to print a <code>Rectangle</code> instance in the format
<code>[Rectangle] (&lt;id&gt;) &lt;x&gt;/&lt;y&gt;</code>.</li>
<li>Public method <code>def update(self, *args, **kwargs):</code> that updates an instance
of a <code>Rectangle</code> with the given attributes.
<ul dir="auto">
<li><code>*args</code> must be supplied in the following order:
<ul dir="auto">
<li>1st: <code>id</code></li>
<li>2nd: <code>width</code></li>
<li>3rd: <code>height</code></li>
<li>4th: <code>x</code></li>
<li>5th: <code>y</code></li>
</ul>
</li>
<li><code>**kwargs</code> is expected to be a double pointer to a dictionary of new
key/value attributes to update the <code>Rectangle</code> with.</li>
<li><code>**kwargs</code> is skipped if <code>*args</code> exists.</li>
</ul>
</li>
<li>Public method <code>def to_dictionary(self):</code> that returns the dictionary
representation of a <code>Rectangle</code> instance.</li>
</ul>
<h3 dir="auto"><a id="user-content-square" class="anchor" aria-hidden="true" href="#square"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Square</h3>
<p dir="auto">Represents a square. Inherits from <code>Rectangle</code> with:</p>
<ul dir="auto">
<li>Class constructor <code>def __init__(self, size, x=0, y=0, id=None):</code>
<ul dir="auto">
<li>The <code>width</code> and <code>height</code> of the <code>Rectangle</code> superclass are assigned using
the value of <code>size</code>.</li>
</ul>
</li>
<li>Overwrite of <code>__str__</code> method to print a <code>Square</code> instance in the format
<code>[Square] (&lt;id&gt;) &lt;x&gt;/&lt;y&gt;</code>.</li>
<li>Public method <code>def update(self, *args, **kwargs):</code> that updates an instance
of a <code>Square</code> with the given attributes.
<ul dir="auto">
<li><code>*args</code> must be supplied in the following order:
<ul dir="auto">
<li>1st: <code>id</code></li>
<li>2nd: <code>size</code></li>
<li>3rd: <code>x</code></li>
<li>4th: <code>y</code></li>
</ul>
</li>
<li><code>**kwargs</code> is expected to be a double pointer to a dictoinary of new
key/value attributes to update the <code>Square</code> with.</li>
<li><code>**kwargs</code> is skipped if <code>*args</code> exists.</li>
</ul>
</li>
<li>Public method <code>def to_dictionary(self):</code> that returns the dictionary
representation of a <code>Square</code>.</li>
</ul>
</article>
