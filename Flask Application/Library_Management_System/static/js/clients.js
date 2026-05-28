<!DOCTYPE html>
<html>

<head>
    <title>Add Book</title>
</head>

<body>

    <h1>Add New Book</h1>

    <form>

        <input type="text" placeholder="Book Name">

        <input type="text" placeholder="Author">

        <input type="text" placeholder="Edition">

        <button type="submit">Add Book</button>

    </form>

</body>
<form>

    <input type="text" id="book_name" placeholder="Book Name">

    <input type="text" id="author" placeholder="Author">

    <input type="text" id="edition" placeholder="Edition">

    <button type="button" onclick="addBook()">
        Add Book
    </button>

</form>

<script src="{{ url_for('static', filename='js/books.js') }}"></script>// CLIENTS JS

function addClient() {

    let clientName = document.getElementById("client_name").value;

    let mobile = document.getElementById("mobile").value;

    let status = document.getElementById("premium_status").value;

    alert(
        "Client Added Successfully\n\n" +
        "Name: " + clientName +
        "\nMobile: " + mobile +
        "\nStatus: " + status
    );
}
</html>