from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random  # Add this import statement

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('flashcards.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    flashcards = conn.execute('SELECT * FROM flashcards').fetchall()
    conn.close()
    return render_template('index.html', flashcards=flashcards)

@app.route('/flashcard/<int:flashcard_id>')
def flashcard(flashcard_id):
    conn = get_db_connection()
    flashcard = conn.execute('SELECT * FROM flashcards WHERE id = ?', (flashcard_id,)).fetchone()
    conn.close()
    if flashcard is None:
        return redirect(url_for('index'))
    return render_template('flashcard.html', flashcard=flashcard)


# New route for the "Lesson One - Words" page
@app.route('/lesson-one')
def lesson_one():
    conn = get_db_connection()
    flashcards = conn.execute('SELECT * FROM flashcards WHERE lesson = ?', ('1',)).fetchall()
    conn.close()
    flashcards_list = [dict(row) for row in flashcards]  # Convert rows to dictionaries
    return render_template('lesson_one.html', flashcards=flashcards_list)

@app.route('/matching-game')
def matching_game():
    conn = get_db_connection()
    flashcards = conn.execute('SELECT * FROM flashcards WHERE lesson = ?', ('1',)).fetchall()
    conn.close()
    flashcards_list = [dict(row) for row in flashcards]  # Convert rows to dictionaries
    # Shuffle flashcards for the game
    import random
    random.shuffle(flashcards_list)
    return render_template('matching_game.html', flashcards=flashcards_list)

@app.route('/typing-game')
def typing_game():
    conn = get_db_connection()
    flashcards = conn.execute('SELECT * FROM flashcards WHERE lesson = ?', ('1',)).fetchall()
    conn.close()
    # Pass the flashcards including the 'arabic' column to the template
    return render_template('typing_game.html', flashcards=flashcards)



if __name__ == '__main__':
    app.run(debug=True)

