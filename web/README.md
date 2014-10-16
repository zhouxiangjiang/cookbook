Web Cookbook
======

HTML

## Getting Started

1. [W3Schools](http://www.w3schools.com/)

## HTML Elements

```html
<!-- Heading -->
<h1> to <h6>

<!-- Paragraph -->
<p title="tool tip">paragraph</p>

<!-- Link -->
<a href="url" target="_self|_blank" title="tool tip">text</a>

<!-- Image -->
<img src="*.jpg|png|gif" alt="alternative text" title="tool tip" />

<!-- Strong/Emphasized/Marked Text -->
<strong>text</strong>
<em>text</em>
<mark>text</mark>

<!-- Line Break -->
<br />

<!-- Horizontal Line -->
<hr />

<!-- Pre-Formatted Text -->
<pre>
    pre-formatted text
</pre>

<!-- Inserted/Deleted Text -->
<ins>text</ins>
<del>text</del>

<!-- Subscript/Superscript -->
<sub>text</sub>
<sup>text</sup>

<!-- Quotations -->
<q>short quotations text</q>
<blockquote>long quotations text</blockquote>

<!-- Details -->
<details> <!-- HTML5, only Chrome support currently -->
    <summary>Summary</summary>
    <p>Details Text</p>
</details>

<!-- Computer Code -->
<code><pre>
    computer code
    <var>variable</var>
</pre></code>

<!-- Computer Output Sample -->
<samp><pre>
    computer output sample
</pre></samp>

<!-- Unordered List -->
<ul>
    <li>list 1</li>
    <li>list 2</li>
</ul>

<!-- Ordered List -->
<ol>
    <li>list 1</li>
    <li>list 2</li>
</ol>

<!-- Abbration -->
The <abbr title="World Health Organization">WHO</abbr>
was founded in 1948.

<!-- Table -->
<table>
    <caption>Table Caption</caption>
    <colgroup> <!-- Columns Formatting -->
        <col span="n" />
        <col span="n" />
    </colgroup>
    <thead>
        <tr>
            <th>head 1</th>
            <th colspan="n" rowspan="m">head 2</th>
        </tr>
    </thead>
    <tfoot>
        <tr>
            <td>col 1</td>
            <td>col 2</td>
        </tr>
    </tfoot>
    <tbody>
        <tr>
            <td>row-1, col-1</td>
            <td>row-1, col-2</td>
        </tr>
        <tr>
            <td>row-2, col-1</td>
            <td>row-2, col-2</td>
        </tr>
    </tbody>
</table>

<!-- Form -->
<form action="." method="post" autocomplete="on|off">

    <!-- input attributes -->
    <!-- autofocus -->
    <!-- required -->

    <!-- Plain Text Field -->
    <label for="var">Input Text 1</label>
    <input type="text" placeholder="default text" title="hint text" name="var" id="var" /><br />

    <!-- Password Field -->
    <label for="var-password">input text for password</label>
    <input type="password" title="hint text"
        name="var-password" id="var-password" />
    <br />
    
    <!-- Range -->
    <input type="range" name="var" id="var" value="default-value" min="" max="" step="" />
    
    <!-- Numebr -->
    <input type="number" name="var" id="var" value="default-value" min="" max="" step="" />
    
    <!-- Color -->
    <input type="color" name="var" />
    
    <!-- Date and Time -->
    <input type="date" name="var" />
    <input type="month" name="var" />
    <input type="week" name="var" />
    <input type="time" name="var" />
    <input type="datetime" name="var" />
    
    <!-- Email Validation -->
    <input type="email" name="var" multiple />

    <!-- Radio Button -->
    <input type="radio" name="var" id="val-1" />
    <label for="val-1">option text 1</label><br />
    <input type="radio" name="var" id="val-2" />
    <label for="val-2">option text 2</label><br />

    <!-- Check Box -->
    <input type="checkbox" name="var" id="val-1" />
    <label for="val-1">option text 1</label><br />
    <input type="checkbox" name="var" id="val-2" />
    <label for="val-2">option text 2</label><br />

    <!-- Text Area -->
    <textarea name="str" rows="x" cols="y" />
    
    <!-- Drop Down List, replacement of <select> elements -->
    <input list="var">
    <datalist id="var">
        <option value="val-1">option 1</option>
        <option value="val-2">option 2</option>
    </datalist>

    <!-- Field Set -->
    <fieldset>
        <legend>legend text</legend>
        <!-- form field elements here ... -->
    </fieldset>

    <!-- Submit Button -->
    <input type="submit" value="display text" />

    <!-- Reset Button -->
    <input type="reset" />

    <!-- Image Button -->
    <input type="image" src="img-url" />
    
    <!-- Output -->
    <!-- in <form>: oninput="x.value=parseInt(a.value)+parseInt(b.value)" -->
    <output name="x" for="a b"></output>

</form>

<!-- Grouping -->
<div>...</div>  <!-- block -->
<span>...</span> <!-- inline -->

<!-- Button -->
<button type="button|reset" autofocus="autofocus" disabled="disabled">Button Text</botton>
<button type="submit" formaction="<url>" formmethod="get|post"
    formenctype="application/x-www-form-urlencoded|multipart/form-data|text/plain">Submit</button>

<!-- Image Map -->
<img src="url" alt="replacement text" title="hint text" usemap="#map-id" />
<map id="map-id">
    <area shape="rect"
        coords="leftTop-x,leftTop-y,rightBottom-x,rightBottom-y"
        alt="repalcement text" title="hint text" href="url-1" />
    <area shape="circle"
        coords="center-x,center-y,radius"
        alt="replacement text" title="hint text" href="url-2" />
</map>

<!-- Video -->
<video width="m" height="n" controls="controls" autoplay="autoplay" loop="loop">
    <source src="*.mp4" type="video/mp4" />
    <source src="*.ogg" type="video/ogg" />
    Your browser does not support the video element.
</video>

<!-- Audio -->
<audio controls="controls">
    <source src="*.ogg" type="audio/ogg" />
    <source src="*.mp3" type="audio/mpeg" />
    Your browser does not support the audio element.
</audio>

<!-- Inline Frame -->
<iframe src="embedded-url" width="x" height="y"
    frameborder="0/1" scrolling="yes/no/auto"
</iframe>
<!-- change iframe elements -->
<iframe src="embedded-url-1"
    width="x" height="y" id="iframe-id"></iframe>
<a href="embedded-url-2" target="iframe-id">Link Text</a>

<!-- More ... -->
<!-- Graphics: <canvas>, <svg> -->
<!-- Geolocation API -->
<!-- Drag and Drop API -->
<!-- Local Storage API: replace cookies -->
<!-- App Cache API -->
<!-- Web Workers -->
<!-- Web SSE -->
```
