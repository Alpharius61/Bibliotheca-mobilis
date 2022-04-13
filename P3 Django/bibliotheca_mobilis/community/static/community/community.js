function checkCount(id) {

    var items = document.getElementById('id_specialities').getElementsByTagName('input')
    var count = 0

    for (i = 0; i < items.length; i++) {

        var currentChild = items[i];

        // now you want to make sure you only retrieve the id's of checkboxes 
        if (currentChild.type.toLowerCase() == "checkbox") {
            if (currentChild.checked == true) {
                count++
            }
        }
    }
    if (count > 3) {
        alert('Seules trois spécialités peuvent être séléctionnées')
        document.getElementById(id).checked = false
    }

}    

function updateRaces(sideId) {
    var xhttp = new XMLHttpRequest();
    var url= document.getElementById('characterCreationForm').getAttribute('data-races-url');
    //  add parameter to GET URL 
    url+= '?sideId=' + sideId

    // function called when server answer arrived 
    xhttp.onreadystatechange = function() {
        // readyState == 4 (done) the request sent and answer received
        // status == 200 the server answer all is ok
        if (this.readyState == 4 && this.status == 200) {

            // update race list against side selection
            document.getElementById('id_race').innerHTML = this.responseText;
            
            // remove null option after first select
            var nullOption = document.getElementById('id_side').getElementsByTagName('option')[0];
            if (nullOption.value == '' ) {
                nullOption.remove();
            };
        };
    }
    xhttp.open("GET", url, true);
    xhttp.send();   
}

