function loadArticle(url) {

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {
    // readyState == 4 (done) the request sent and answer received
    // status == 200 the server answer all is ok
    if (this.readyState == 4 && this.status == 200) {

        // rebuild page Article 
        container = document.getElementById('historyContainer');
        menu=container.getElementsByClassName('itemTreeMenu')[0];
        // Add article
        container.innerHTML = this.responseText;
        // Add Menu on top
        container.prepend(menu);
    };
}
xhttp.open("GET", url, true);
xhttp.send();
}
