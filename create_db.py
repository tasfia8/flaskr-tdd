# create_db.py


from project.app import app, db
from project.models import Post


with app.app_context():
    # create the database and the db table
    db.create_all()
    print("Testing: Database and tables created successfully!")

    # Post model used to insert a dummy post to ensure it's recognized in createdb.py file
    dummy_post = Post(title="Dummy Post", text="This is a dummy post.")
    db.session.add(dummy_post)

    # commit the changes
    db.session.commit()
    print("Dummy post added to the Post table!")
