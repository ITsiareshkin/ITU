// Author Danylo Pimenov, xpimen00
function get_week(){

    let an_id = document.getElementById("animal_id"); 
    let animal_id = an_id.attributes.item(1).nodeValue;

    let week_number = an_id.textContent;

    let d = new Date();
    let year = d.getFullYear();
    let walk_data = "week_number="+week_number +"&year_number="+year+"&animal_id="+animal_id;

    url_a = "/walk_week/";
    $.ajax({
        type: 'GET',
        url: url_a,
        data: walk_data,
        success: function (response) {
            
            var days = JSON.parse(response["days"]);
            if(days.length == 0) {
                window.alert("41");
            }else {
                for (let i = 0; i < days.length; i++) {

                    var fields = days[i]["fields"];
                    let cut_date = fields["date"].slice(5);
                    document.getElementById(i+1).textContent =  cut_date.slice(3,6) + "." + cut_date.slice(0,2);
                    if (fields["time"]!=null ) {
                        let fr_tm = fields["time"].slice(0,2);
                        let se_tm = fields["time"].slice(8,10);  
                        let entr_id1 = i+1 + fr_tm;
                        let entr_id2 = i+1 + se_tm;
                        entr_id2 -= 1;
                        if (entr_id2 - entr_id1 > 1){
                            document.getElementById(entr_id1).style.backgroundColor = "rgba(189, 119, 91, 0.8)";
                            document.getElementById(entr_id2-1).style.backgroundColor = "rgba(189, 119, 91, 0.8)";
                            document.getElementById(entr_id2).style.backgroundColor = "rgba(189, 119, 91, 0.8)";

                            document.getElementById(i+1).style.backgroundColor = "rgba(231, 169, 87, 0.8)";
                            
                        }  else {

                            if (entr_id1 - entr_id2 == 0){
                                document.getElementById(entr_id1).style.backgroundColor = "rgba(189, 119, 91, 0.8)";

                                document.getElementById(i+1).style.backgroundColor = "rgba(231, 169, 87, 0.8)";
                            }

                            document.getElementById(entr_id1).style.backgroundColor = "rgba(189, 119, 91, 0.8)";
                            document.getElementById(entr_id2).style.backgroundColor = "rgba(189, 119, 91, 0.8)";

                            document.getElementById(i+1).style.backgroundColor = "rgba(231, 169, 87, 0.8)";

                        }

                    }

                }
                    
                
            }

           //window.alert(response);

        },
        error: function (response) {
            alert(response["responseJSON"]["error"]);
        }
    })


}

var counetr = 0;
var id0=0, id1=0, id2=0;

function send_shed(){

    let an_id = document.getElementById("animal_id"); 
    let animal_id = an_id.attributes.item(1).nodeValue;

    if (counetr>0){
        if (counetr==3 ){

            time = id2%100 + ":00 - " + (id0%100+1) + ":00";

        } else{

            if (counetr==2){
                time = id1%100 + ":00 - " + (id0%100+1) + ":00";

            }else{

                time = id0%100+ ":00 - " + (id0%100+1) + ":00";

            }
        
        }
    }


    let day = document.getElementById(Math.floor(id0/100)).textContent;

   // console.log(day);
   // console.log(time);

    url_a = "/walk_register/";
   let walk_param = "time="+time +"&day="+day+"&animal_id="+animal_id;
   $.ajax({
    type: 'GET',
    url: url_a,
    data: walk_param,
    success: function (response) {
        
        get_week();
       //window.alert(response);

    },
    error: function (response) {
        alert(response["responseJSON"]["error"]);
    }
})
   

}

function newShed(id){

    if (id == "week_1"){
        let week_num = document.getElementById("animal_id").textContent; 
        document.getElementById("animal_id").textContent = document.getElementById("week_num").textContent;  
    }
    
    if (id == "week_2"){
        let week_num = document.getElementById("animal_id").textContent; 
        document.getElementById("animal_id").textContent = +document.getElementById("week_num").textContent+1;  
    }

    if (id == "week_3"){
        let week_num = document.getElementById("animal_id").textContent; 
        document.getElementById("animal_id").textContent = +document.getElementById("week_num").textContent+2;  
    }

    if (id == "week_4"){
        let week_num = document.getElementById("animal_id").textContent; 
        document.getElementById("animal_id").textContent = +document.getElementById("week_num").textContent+3;  
    }

    clear_table()
    get_week();
    
}

function clear_table(){

    for( let i=1; i<=5; i++){

        for(let g=8; g<=9; g++){

            //console.log( i.toString() + "0" + g.toString() );
            document.getElementById(i.toString() + "0" + g.toString()).style.backgroundColor = "transparent";

        }
        
        for( let j=10; j<=19; j++){

            //console.log(i.toString()+j.toString());
            document.getElementById(i.toString()+j.toString()).style.backgroundColor = "transparent";

        //document.getElementById(i.toString()+j.toString()).style.backgroundColor = "transparent";

        }

       // document.getElementById(i.toString()).style.backgroundColor = "white";
        document.getElementById(i.toString()).style.backgroundColor = "transparent";


    }

}

function sheduleFunction(id) {

    //&& document.getElementById(Math.floor(id/100)).style.backgroundColor !== rgba(231, 169, 87, 0.8)
    if (counetr<3 && (document.getElementById(Math.floor(id/100)).style.backgroundColor !== rgba(231, 169, 87, 0.8)) ) {

        if ( document.getElementById(id).style.backgroundColor !== "rgba(112, 162, 242, 0.8)" ){
            id2 = id1;
            id1 = id0;
            id0 = id;
            if ( id1!=0 && (id0 < id1 || id0-id1 != 1 )){
                id0 = id1;
                id1 = id2;
                id2 = 0;
            } else {
                document.getElementById(id).style.backgroundColor = "rgba(112, 162, 242, 0.8)";
            counetr++;
            
            }

        } else {

            if ( id!==id1 && id !==id2 ) {
                document.getElementById(id).style.backgroundColor= "transparent";
                counetr--;
                id0 = id1;
                id1 = id2;
                id2 = 0;
            }
            
        }
          
        if (counetr==3 && id0!=0){
            document.getElementById(Math.floor(id0/100)).style.backgroundColor= "rgba(231, 169, 87, 0.8)"; 
            } else {
                document.getElementById(Math.floor(id0/100)).style.backgroundColor= "transparent";
            }

    } else {

        if ( document.getElementById(id).style.backgroundColor == "rgba(112, 162, 242, 0.8)" ){
            
            if ( id!==id1 && id !==id2 ) {
                document.getElementById(id).style.backgroundColor= "transparent";
                counetr--;
                id0 = id1;
                id1 = id2;
                id2 = 0;
            }

        }
            if (counetr==3){
                document.getElementById(Math.floor(id0/100)).style.backgroundColor= "rgba(231, 169, 87, 0.8)"; 
            } else {
                document.getElementById(Math.floor(id0/100)).style.backgroundColor= "transparent";
            }
    }
   


}




$(document).ready(get_week());