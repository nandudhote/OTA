from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route("/sp16")
def return_pdf():
    # Get the list of files in the current directory
    files = os.listdir(".")
    
    # Filter for the file with the .hex extension (or use other criteria)
    filename = next((file for file in files if file.endswith(".hex")), None)
    print (filename)
    # If the file is found, return it
    if filename:
        return send_file(filename)
    else:
        return "File not found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1000)
