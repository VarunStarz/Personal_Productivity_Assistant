import os
from dotenv import load_dotenv
from Backend.model import getResponse
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

load_dotenv()

os.system('python C:/Users/saico/Downloads/Varun/MyProjects/LangChainAgentsProject/Personal_Productivity_Assistant/Backend/IngestData.py')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def queryAssistant():
    data = request.get_json()
    query = data['query']
    print(f'user query ---> {query}')

    if not query:
        return jsonify({'error': 'Query cannot be empty'}), 400
    
    response = getResponse(query=query)
    print(f'user response ---> {response}')
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)