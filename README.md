# BooksCrudApp
Book Summary is a simple Django application tailored to meet the needs of users who want to write,post or remember a certain book they read.The site allows users to view, post, delete , update and even create a new book.

### Author: Maureen Wairimu

## User Story
<ul>
<li>Users can create a new book summary. </li>
<li>Users can read/view the book summarys' they created.</li>
<li>Users can update an existing book summary.</li>
<li>Users can delete a book summary they created. </li>
</ul>


## Behavior Driven Development (BDD)

Behavior                 |Input                            |Output                             |
|------------------------|----------------------------------|----------------------------------|
|The landing page loads  |Users scroll | Users see available book summaries|
|The book app loads  |Users click on the delete icon or update icon next to the summary they created|Users see their updated or deleted book on the landing page|
|The landing page loads  |Users click on the + icon and write their summary|The book will be uploaded and displayed to landing page|


## Setup Instructions

<ol>
<li> Clone this repo: git clone <code>gh repo clone maureen28/BooksCrudApp </code> </li>
<li>The repo comes in a zipped or compressed format. Extract to your prefered location and open it.</li>
<li> Create a virtual environment and activate it.
<pre>
<code>
pip install virtualenv
source virtual/bin/activate
</code></pre>
</li>
<li> Install all the requirements <code> pip install -r requirements.txt</code></li>
<li> On your terminal,Create database aaward using the command :<code>CREATE DATABASE book; and update settings.py </code>
</li>
<li> Migrate the database using the command : <code> python3.6 manage.py migrate </code> </li>
<li> Run <code>python3 manage.py runserver</code> to serve the app.</li>
<li> Use the navigation bar menu to navigate and explore the app.</li>
</ol>
