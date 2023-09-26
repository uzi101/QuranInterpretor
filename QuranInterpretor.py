from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS

def modify_quran_text(filename="QuranEnglish_original.txt", new_filename="QuranEnglish.txt"):
    with open(filename, "r") as file:
        lines = file.readlines()
    new_lines = [line.strip() + "\n\n" for line in lines]
    with open(new_filename, "w") as file:
        file.writelines(new_lines)

def load_quran_text(filename):
    with open(filename, "r") as file:
        quran_text = file.read()
    return quran_text.split("\n\n")

def find_relevant_verse_ml(question, verses, vectorizer, tfidf_matrix):
    query_vector = vectorizer.transform([question])
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix)
    most_similar_verse_index = cosine_similarities.argmax()

    # Get the relevant verse and the next two verses if they exist
    start_index = most_similar_verse_index
    end_index = min(most_similar_verse_index + 3, len(verses))
    context_verses = verses[start_index:end_index]

    return " ".join(context_verses)

app = Flask(__name__)
CORS(app, resources={r"/ask": {"origins": "http://localhost:3000"}})

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Quran Interpretor!"

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.json.get('question')
    if not question:
        return jsonify({'error': 'Invalid input'}), 400

    relevant_verse = find_relevant_verse_ml(question, quran_verses, vectorizer, tfidf_matrix)
    if relevant_verse:
        return jsonify({'relevant_verse': relevant_verse})
    else:
        return jsonify({'message': 'No relevant verse found for this question.'})

if __name__ == '__main__':
    modify_quran_text()
    quran_verses = load_quran_text("QuranEnglish.txt")
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(quran_verses)
    app.run(debug=True)
