var comanda = document.getElementById("comanda");
if (comanda) {
    for (var i=0; i < month.length;++i){
        addOption(comanda, month[i], month[i]);
    }
}

addOption = function(selectbox, text, value) {
    var optn = document.createElement("OPTION");
    optn.text = text;
    optn.value = value;
    selectbox.options.add(optn);
}