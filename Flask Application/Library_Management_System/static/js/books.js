// MAIN JS FILE

console.log("Library Management System Loaded");

// Welcome alert
window.onload = function () {
// BOOKS JS

function addBook() {

    let bookName = document.getElementById("book_name").value;

    let author = document.getElementById("author").value;

    let edition = document.getElementById("edition").value;

    alert(
        "Book Added Successfully\n\n" +
        "Book: " + bookName +
        "\nAuthor: " + author +
        "\nEdition: " + edition
    );
}
    console.log("Welcome to LMS");

};