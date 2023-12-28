from flask import Flask, render_template, url_for, request, jsonify
from text_sentiment_prediction import *

#libreria para exponer la api a una url publica
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

# correr la api en url publica
run_with_ngrok(app)

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    
    # Obtener el texto ingresado del requerimiento POST.
    input_text = request.json.get("text")  
    
    if not input_text:
        # Respuesta para enviar si input_text está indefinido.
        response = {
                    "status": "error",
                    "message": "¡Por favor, ingresa algún texto para predecir la emoción!"
                  }
        return jsonify(response)
    else:  
        predicted_emotion,predicted_emotion_img_url = predict(input_text)
        
        # Respuesta para enviar si input_text no está indefinido.
        response = {
                    "status": "success",
                    "data": {
                            "predicted_emotion": predicted_emotion,
                            "predicted_emotion_img_url": predicted_emotion_img_url
                            }  
                   }

        # Enviar respuesta.         
        return jsonify(response)
       
app.run()




    