from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# واجهة المستخدم الخاصة باللاب
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>CyberJocx - Ping Diagnostic Tool</title>
    <style>
        body { font-family: Arial, sans-serif; background: #121212; color: #00ffcc; text-align: center; padding-top: 50px; }
        .card { background: #1e1e1e; padding: 20px; display: inline-block; border-radius: 8px; box-shadow: 0 0 10px #00ffcc; }
        input[type=text] { padding: 10px; width: 250px; border-radius: 4px; border: 1px solid #00ffcc; background: #000; color: #fff; }
        input[type=submit] { padding: 10px 20px; border: none; background: #00ffcc; color: #000; font-weight: bold; cursor: pointer; border-radius: 4px; }
        pre { background: #000; color: #00ff00; padding: 15px; text-align: left; display: inline-block; width: 80%; overflow-x: auto; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Network Ping Tool</h2>
        <form method="POST">
            <input type="text" name="ip" placeholder="Enter IP address (e.g. 127.0.0.1)" required>
            <input type="submit" value="Ping">
        </form>
    </div>
    {% if output %}
    <h3>Output:</h3>
    <pre>{{ output }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    output = ""
    if request.method == 'POST':
        ip = request.form.get('ip')
        # الثغرة هنا: استخدام مدخلات المستخدم مباشرة في أمر النظام
        command = f"ping -c 1 {ip}"
        try:
            output = os.popen(command).read()
        except Exception as e:
            output = str(e)
            
    return render_template_string(HTML_TEMPLATE, output=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
