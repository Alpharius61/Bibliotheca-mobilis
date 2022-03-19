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
