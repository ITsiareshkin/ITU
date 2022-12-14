// Author: Dmytro Sadovskyi, xsadov06
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
                        donation_item+="<a onclick='end_f(" + donations[i]["pk"] + ")' href='#'</a> End</div>";
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

function end_f(id){
    let url_a = "/end_donation/";
    $.ajax({
        type: 'GET',
        url: url_a,
        data: "id="+id,
        success: function (response) {
            load_donations();
            update_values();
        },
        error: function (response) {
            alert(response["responseJSON"]["error"]);
        }
    })
}

$("#donation_form").submit(function (e) {
    e.preventDefault();
    let serializedData = $("#donation_form").serialize();
    let url_a = "/add_fundraising/";
    $.ajax({
        type: 'GET',
        url: url_a,
        data: serializedData,
        success: function (response) {
            const popupActive = document.querySelector('.popup.open');
            popupClose(popupActive, true);
            window.alert("Created successfully ");
            load_donations()
            document.getElementById("donation_form").reset();
        },
        error: function (response) {
            alert(response["responseJSON"]["error"]);
        }
    })
})