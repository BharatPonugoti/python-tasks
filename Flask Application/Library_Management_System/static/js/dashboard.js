<!DOCTYPE html>
<html>

<head>
    <title>Add Client</title>
</head>

<body>

    <h1>Add Client</h1>

    <form>

        <input type="text" placeholder="Client Name">

        <input type="text" placeholder="Mobile Number">

        <select>
            <option>Paid</option>
            <option>Not Paid</option>
        </select>

        <button type="submit">Add Client</button>

    </form>

</body>
<form>

    <input type="text" id="client_name" placeholder="Client Name">

    <input type="text" id="mobile" placeholder="Mobile Number">

    <select id="premium_status">

        <option>Paid</option>

        <option>Not Paid</option>

    </select>

    <button type="button" onclick="addClient()">
        Add Client
    </button>

</form>

<script src="{{ url_for('static', filename='js/clients.js') }}"></script>// DASHBOARD JS

console.log("Dashboard Loaded");

// Dashboard welcome message
document.addEventListener("DOMContentLoaded", function () {

    alert("Welcome Admin 👋");

});
</html>