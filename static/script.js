//const de index
const nameUser = document.getElementById("nameUser");
const sendName = document.getElementById("sendName");

const titleBook = document.getElementById("titleBook");
const authorName = document.getElementById("authorName");
const genre = document.getElementById("genre");
const addBook = document.getElementById("addBook");

const searchBox = document.getElementById("searchBox");
const searchButton = document.getElementById("searchButton");

const wish = document.getElementById("wish");
const wishButton = document.getElementById("wishButton");

const count = document.getElementById("count");

const textarea = document.getElementById("textarea");


// //functions for the username and welcome/back username

//function to add the username to localStorage and say welcome user
function welcomeUsername(){

    let username = nameUser.value;
    localStorage.setItem("username", username);

    let actual_username = localStorage.getItem("username");
    let welcome = document.getElementById("welcome")

    actual_username.innerHTML = nameUser.value;
    welcome.innerHTML += actual_username
    document.getElementById("nameDiv").style.display = 'none';
}
sendName.addEventListener("click", welcomeUsername,); 


//function to say welcome back username
function welcomeBack(){
    let username = localStorage.getItem("username");
    let welcome = document.getElementById("welcome");
    
    if (localStorage.key("username") === null || localStorage.getItem("username") === null){
        welcome.innerHTML = "Welcome "
    } else if (localStorage.getItem("username") === "" ){
        welcome.innerHTML = "Welcome "
    } else {
        welcome.innerHTML += " back " + username;
        document.getElementById("nameDiv").style.display = 'none';
    }
}

welcomeBack(); 


//function to add the number of books in the library
function clickAddCount(){
    let nbBooks = localStorage.getItem("books");
    if (nbBooks == null){
        localStorage.setItem("books", 0);
    }nbBooks++
    localStorage.setItem("books", nbBooks);
}
    
//function to refresh the main page everytime with the nb of books
function refreshMainPage(){
    let nbBooks = localStorage.getItem("books");
    
    if (nbBooks != null ){
        nbBooks = parseInt(nbBooks)
        document.getElementById("countClick").innerHTML = nbBooks;
        if (nbBooks ==1){
            document.getElementById("bookChange").innerHTML = " book";
        } else{
            document.getElementById("bookChange").innerHTML = " books";
        } 
    }else if (nbBooks == 0){
            document.getElementById("bookChange").innerHTML = " book";
            document.getElementById("countClick").innerHTML = nbBooks;
        }
        
    } 
refreshMainPage();

addBook.addEventListener("click", clickAddCount);


//function to display the date
function setDate(){
    let dateGlobale = new Date();
    let year = dateGlobale.getFullYear();
    let month = dateGlobale.getMonth();
    let date = dateGlobale.getDate();
    let day_name = dateGlobale.getDay();

    let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    let months = ["January", "February","March", "April", "May", "June", "July", "August", "September", 
                    "October", "November", "December"];
    month = months[month];
    day_name = days[day_name];
    document.getElementById("date").innerHTML = day_name + " " + date + " " + month + " " + year;                
}
setDate()

