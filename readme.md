This is a newsreader application.

It has following features

1) It Showcase the list of articles with the headline, date in a neat vertically scrollable list
2) On clicking an article, the clean text view of the article opens and one can close it to go back to the original list view
3) One can annotate any part of the text of the article - Highlight and/ or Comment specific parts of the text. The annotations are stored, and reappear next time when opening it.
4) It uses first 5 words of the description as the "headline" field
5) feed list is sorted according to the date in descending order.

SETUP:-

Install Python, Django and Mongodb.

Then install Django MongoDB Engine and virtualENV according to the following link

http://django-mongodb-engine.readthedocs.org/en/latest/topics/setup.html

Now download this git package

https://github.com/sawangupta92/staticfiles

unzip the folder.

cd inside the folder

run following commands

1) python setup.py build

2) sudo python setup.py install 

Now download our newsreader application

https://github.com/sawangupta92/NewsReader

unzip the folder.

cd inside the folder

run python manage.py syncdb

cd where article_dump.json is saved.

run 

1) mongoimport -d newsreader -c nread_feed article_dump.json

2) mongo

3) db.nread_feed.find().forEach( function(m) {db.description.update({_id:m._id},{$set:{ww:new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()))}}) } );

4) db.nread_feed.ensureIndex({"date":-1})

5) ctrl-c

now cd again to manage.py file

1) python manage.py collectstatic

2) python manage.py runserver