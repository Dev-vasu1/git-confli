<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample HTML Page</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            margin-top: 50px;
        }

        .card {
            background: green;
            padding: 20px;
            width: 300px;
            margin: auto;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        button {
            padding: 10px 15px;
            border: none;
            background: blue;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background: darkblue;
        }
    </style>
</head>
<body>

    <div class="card">
        <h1>Welcome!</h1>
        <p>This is a sample HTML page.</p>

        <button onclick="showMessage()">
            Click Me
        </button>
    </div>

    <script>
        function showMessage() {
            alert("Hello from JavaScript!");
        }
    </script>

</body>
</html>
