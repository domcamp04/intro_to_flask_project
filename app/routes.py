from app import app
from flask import render_template


@app.route('/') 
def index():
    name = 'Dominick\'s Favorite 5'
    title = 'Home'
    return render_template('index.html', title=title)

@app.route('/favorites')
def test():
    title = 'Five Favorite Bands'
    favorites = ['Chciago', 'The Eagles', 'Wings', 'Ace', 'Elo']
    return render_template('favorites.html', title=title, favorites=favorites)