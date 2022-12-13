function set_form_value(id){
    var d_input = document.getElementById("d_id");
    d_input.value=id;
}

function load_donations(){
    var serializedData = $("#filter").serialize();
    let url_a = "/donations/";
    $.ajax({
        type: 'GET',
        url: url_a,
        data: serializedData,
        success: function (response) {
            document.getElementById("donations_list").innerHTML = "";
            var theDiv = document.getElementById("donations_list");
            var donations = JSON.parse(response["donation"]);
            if(donations.length == 0) {
                theDiv.innerHTML += "Not Found"
            }else {
                for (let i = 0; i < donations.length; i++) {
                    var fields = donations[i]["fields"];
                    var donation_item = "<div class=\"progress\">" + fields["description"] + "<br>" + fields["current_amount"] + " of " + fields["amount"] + " donated" + "<div class=\"progress-back\">" + "<div class=\"progress-bar\" id='" + i + "'></div></div>";
                    if(fields["end"]==false){
                        donation_item+="<a class='popup-link' onclick='set_form_value(" + donations[i]["pk"] + ")' href='/donate/'</a> Donate</div>";
                    }else{
                        donation_item+="</div>";
                    }
                    theDiv.innerHTML += donation_item;
                    let width = ((+(fields["current_amount"])) / (+(fields["amount"])))*100;
                    if(width > 100){
                        width = 100;
                    }
                    document.getElementById(i.toString()).style.width= width.toString() + "%";
                }
                update_values();
            }
        },
        error: function (response) {
            alert(response["responseJSON"]["error"]);
        }
    })
}

$("#donation_form").submit(function (e) {
    e.preventDefault();
    var frm = $('#donation_form');
    var formData = new FormData(frm[0]);
    let url_a = "/donate/";
    $.ajax({
        type: 'POST',
        url: url_a,
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
            const popupActive = document.querySelector('.popup.open');
            popupClose(popupActive, true);
            window.alert("Thank you for your donation");
            let addr = window.location.toString();
            load_donations()
            document.getElementById("donation_form").reset();
        },
        error: function (response) {
            alert(response["responseJSON"]["error"]);
        }
    })
})