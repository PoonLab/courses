# Markdown

## What is Markdown?
Markdown is a simple markup language (get it?).  A markup language is a set of rules for annotating a text document with additional information such as formatting or hierarchical relationships (*i.e.,* X is a member of Y).  The [Hypertext markup language](https://en.wikipedia.org/wiki/HTML) (HTML) is probably the most widely-known markup language.  In HTML, plain text can be enclosed by tags that define a context for the text; for example, `<b>foo</b>` renders the word **foo** in bold face.  A simple HTML document looks something like this:
```html
<html>
  <h1>A simple HTML document.</h1>
  <p>
    Here is some <b>content</b>.
    Here is some <i>more</i> content, and here is an itemized list:
    <ul>
      <li>red</li>
      <li>green</li>
      <li>blue</li>
    </ul>
  </p>
</html>
```

When this HTML is rendered by a web browser, it looks like this:
  <h1>A simple HTML document.</h1>
  <p>
    Here is some <b>content</b>.
    Here is some <i>more</i> content, and here is an itemized list:
    <ul>
      <li>red</li>
      <li>green</li>
      <li>blue</li>
    </ul>
  </p>

Writing out all those enclosing tags can be a bit of a pain, and it gets worse when we want to do something more complicated like nested lists or tables.  [Markdown](https://en.wikipedia.org/wiki/Markdown) was developed in 2004 as a way to write readable documents that could be readily converted into HTML.  The Markdown for making an HTML page equivalent to the previous code looks like this:
```markdown
# A simple HTML document
Here is some **content**.
Here is some *more* content, and here is an itemized list:
* red
* green
* blue
```
Not only is there less extraneous markup text, but it doesn't interfere with our ability to read the underlying plain text.

Markdown has become widely adopted.  For example:

* [GitHub](github.com) -- the largest code hosting service in the world -- uses Markdown as the standard format for developers to communicate with each other about coding issues.  
* [RStudio](https://www.rstudio.com/) provides [R Markdown](https://rmarkdown.rstudio.com/) as a simple format for creating rich documents with embedded R analyses and figures.  
* [Jekyll](https://en.wikipedia.org/wiki/Jekyll_(software)) is a [Ruby](https://en.wikipedia.org/wiki/Ruby_(programming_language))-based framework for authoring [static web pages](https://en.wikipedia.org/wiki/Static_web_page), such as a blog site, using Markdown files and a small set of common templates.  In fact, you're reading a Markdown file right now - if you're looking at this in your web browser, then it has probably been rendered into an HTML document by Jekyll.  
* Some JavaScript frameworks for authoring web-based "PowerPoint" presentations, such as [reveal.js](https://revealjs.com/#/), can use Markdown for writing slides.

A Markdown file is conventionally given the file extension `.md`.  When you see a file named `README.md`, then you can expect to be able to open it as a plain text file in any editor application and see some text decorated with Markdown syntax.


## Markdown syntax
One of the tricky aspects of Markdown is that there are multiple implementations of the language.  There are also markup languages that extend Markdown by providing additional features such as the ability to embed mathematical formulas or bibliographies.  That means that an annotation that is recognized by one implementation of Markdown won't necessarily be recognized by another. 

![](https://imgs.xkcd.com/comics/standards.png)

However, there is some basic syntax that is fairly global across these different implementations and extensions.  Given the current popularity of Markdown, there are several guides and resources online, but for your convenience I will summarize some of this syntax here.  You can also look at the Markdown source of these Readings by clicking on the `Raw` button and compare this file alongside the rendered HTML.

### Headings

```markdown
# A top level heading (title)
## Second level heading
### Third level, and so on
```
I'm not going to show the HTML rendering of these headers because it will mess up the document format.


### Text formatting
```markdown
*italics*
**bold**
__underline__
~~strikethrough~~
```
*italics*
**bold**
__underline__
~~strikethrough~~

### Lists
```markdown
* First item in a bulleted list
* Another item
1. Now we're switching to a numbered list
2. Here is the next entry
```
* First item in a bulleted list
* Another item
1. Now we're switching to a numbered list
2. Here is the next entry

### Tables and rules
```markdown
| Tables | are | a | bit |
|--------|-----|---|-----|
| of     | a   | bear | to |
| write | in | markdown | but |
| still | a | lot | easier | 
| than | HTML | ! | |
```
| Tables | are | a | bit |
|--------|-----|---|-----|
| of     | a   | bear | to |
| write | in | markdown | but |
| still | a | lot | easier | 
| than | HTML | ! | |

```markdown
To draw a horizontal rule across the page, we use a triple dash:

---

which is handy for separating sections in the text.  Careful: if we don't have line breaks separating the text from the triple dash, then a Markdown interpreter may render the first line as an H2 header.
```
To draw a horizontal rule across the page, we use a triple dash:

---

which is handy for separating sections in the text.

### Links and images
```markdown
[This embeds a link in the document](http://github.com)
![This embeds an image in the document through its URL](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/200px-Octicons-mark-github.svg.png)
```
[This embeds a link in the document](http://github.com)
![This embeds an image in the document through its URL](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/200px-Octicons-mark-github.svg.png)

### Code blocks
Blocks of code can be displayed in Markdown by enclosing the code in a pair of triple backticks ` ``` `.  We name a programming language after the first set of triple backticks to tell Markdown how to interpret the code for syntax highlighting.
````markdown
 ```python
 for i in range(100):
     print ('pants!')
 ```
````
 ```python
 for i in range(100):
     print ('pants!')
 ```

## Editors
You can use any text editor to write Markdown as a plain text file, but it can be helpful to use a special editor that recognizes the Markdown syntax and modifies how your text is rendered accordingly.  For Linux, `gedit` is a simple text editor that does a nice job of highlighting headers, formatted text and lists; for command-line text editing, I quite like `vim`.  For more expressive editors, you might try some open-source web applications such as:
* [stackedit.io](https://stackedit.io/app#)
* [dillinger.io](https://dillinger.io/)

![](https://imgs.xkcd.com/comics/types_of_editors.png)
