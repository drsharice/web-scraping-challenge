# 1. import modules
from flask import Flask
import scrape_mars


# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017")


# Connect to a database. Will create one if not already available.
db = mongo.scrape_db

# Creates a collection in the database and inserts two documents
db.scrape.insert_many(
    [
        {
            'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg', 
            'title': 'Syrtis Major Hemisphere Enhanced'
        },
        {
            'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',
           'title': 'Syrtis Major Hemisphere Enhanced'
        },

         {
            'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg', 
            'title': 'Syrtis Major Hemisphere Enhanced'
        }
    ]
)




# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()

    # Return the template with the teams list passed in
    return render_template('index.html', destination_data)


@app.route("/scrape")
def scrape():

    # Run the scrape function
    scape_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, scape_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

