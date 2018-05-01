# Markdown

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

Markdown has become widely adopted.  For example, [GitHub](github.com) -- the largest code hosting service in the world -- uses Markdown as the standard format for developers to communicate with each other about coding issues.  
