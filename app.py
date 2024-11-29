from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__)

# مسار ملف JSON الذي يحتوي على الملاحظات
notes_file = 'messages.json'

# التحقق مما إذا كان ملف JSON موجودًا
if not os.path.exists(notes_file):
    with open(notes_file, 'w') as f:
        json.dump([], f)

# تحميل الملاحظات من ملف JSON
@app.route('/messages.json', methods=['GET'])
def get_notes():
    with open(notes_file, 'r') as f:
        notes = json.load(f)
    return jsonify(notes)

# حفظ الملاحظات إلى ملف JSON
@app.route('/save-notes', methods=['POST'])
def save_notes():
    try:
        new_notes = request.get_json()
        with open(notes_file, 'w') as f:
            json.dump(new_notes, f)
        return jsonify({'message': 'Notes saved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# توفير الصور من المجلد
@app.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

# تشغيل التطبيق
if __name__ == '__main__':
    app.run(debug=True)
