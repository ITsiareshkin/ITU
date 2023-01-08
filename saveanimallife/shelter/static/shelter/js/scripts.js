// Author: Dmytro Sadovskyi, xsadov06
function page_change(id){
    var serializedData = $("#filter").serialize();
    let url_a = "/animals/?page="+id.toString();
    $.ajax({
        type: 'GET',
        url: url_a,
        data: serializedData,
        success: function (response) {
            document.getElementById("animal_list").innerHTML = "";
            var theDiv = document.getElementById("animal_list");
            var animals = JSON.parse(response["animal"]);
            if(animals.length == 0) {
                theDiv.innerHTML += "Not Found"
            }else {
                for (let i = 0; i < animals.length; i++) {
                    var fields = animals[i]["fields"];
                    var animal_item = "<div class=\"animal-item\"><a href=\"" + "" + animals[i]["pk"] + "/\"><div class=\"animal-image-list\"><img src=\"/media/" + fields["photo"] + "\" alt=\"\"></div><div class=\"animal-description-\"><div class=\"animal-name-list \">" + fields["name"] + "</div><div class=\"animal-info-list\">" + fields["gender"] + " / " + fields["age"] + " y.o</div></div></a></div>"
                    theDiv.innerHTML += animal_item;
                }
            }
            var pages = JSON.parse(response["pages"]);
            var page_n = document.getElementById("pagelist");
            document.getElementById("pagelist").innerHTML = "";
            if(Number(pages[0]["pages"]) > 1) {
                for (let i = 1; i <= Number(pages[0]["pages"]); i++) {
                    var page_item;
                    if (i != pages[1]["page"]) {
                        page_item = "<input type=\"button\" onclick=\"page_change(" + i.toString() + ")\" value=\"" + i.toString() + "\" class=\"page-num\"/>";
                    } else {
                        page_item = "<input type=\"button\" onclick=\"page_change(" + i.toString() + ")\" value=\"" + i.toString() + "\" class=\"page-num-selected\"/>";
                    }
                    page_n.innerHTML += page_item;
                }
            }
        },
        error: function (response) {
            alert(response["responseJSON"]["error"]);
        }
    })
}

