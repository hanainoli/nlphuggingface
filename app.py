from flask import Flask, request, jsonify
from pydub import AudioSegment
import tempfile
import os

app = Flask(__name__)

@app.route('/process_audio', methods=['POST'])
def process_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    audio_file = request.files['file']

    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'})

    if audio_file:
        try:
            # Save the audio file to a temporary location
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
                temp_audio_path = temp_audio.name
                audio_file.save(temp_audio_path)

                # Process the audio file (Example: Getting duration)
                audio = AudioSegment.from_file(temp_audio_path)
                duration_ms = len(audio)

                # You can perform any other processing here...

            # Prepare JSON response
            response = {
                'duration_ms': duration_ms,
                # Add any other processed data to the response
            }
            
            return jsonify(response)

        except Exception as e:
            return jsonify({'error': str(e)})
        finally:
            # Delete temporary file
            if os.path.exists(temp_audio_path):
                os.unlink(temp_audio_path)

    return jsonify({'error': 'Unknown error'})

if __name__ == '__main__':
    app.run(debug=True)
