var circuit = [
]
// var circuit = [
//     ["item1","position1","element1"],
//     ["item12","position1","element1"],
//     ["item14","position1","element1"],
// ]
function refresh(xlst){
    x = JSON.stringify(xlst)
$.ajax({
    type: "POST",
    url: "/getsvg",
    data: { 
        circuitlst: x,
        csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val(),
    },
    success: function(result) {
        document.getElementsByClassName("circuitarea")[0].innerHTML = String(result["circuitsvg"]);
        document.getElementsByClassName("circuitarea")[0].innerHTML += `<button onclick="download()" id="DownloadBtn">Download</button>`;
    },
    error: function(result) {
        alert(error)
    }
});
}
function refreshlist(){
    document.getElementsByClassName("list")[0].innerHTML = ``;
    for(element of circuit){
        document.getElementsByClassName("list")[0].innerHTML += `<div class="alert alert-success" style="display: table;">
        <span class="badge bg-primary">${element[0]}</span
        ><span class="badge bg-warning text-dark">${element[1]}</span
        ><span class="badge bg-success">${element[2]}</span
        ><button onclick="removeelement(${element[3]})" type="button" class="btn-close removeButton"data-bs-dismiss="alert"aria-label="Close"></button></div>`;
    }
}
var latestPk = 0;
function addElement(){
    latestPk += 1;
    let x = [$("#elementSelect").val(),$("#positionSelect").val(),$("#LabelText").val()];
    x.push(latestPk);
    circuit.push(x);
    refreshlist();
    refresh(circuit);
};
function removeelement(pk){
    for (element of circuit){
        if(element[3] == pk){
            circuit.splice(circuit.indexOf(element),1)
        }
    }
    refreshlist();
    refresh(circuit);
};
function download(){
    var canvas = document.getElementsByTagName("canvas")[0];
    canvas.setAttribute("width", document.getElementsByTagName("svg")[0].getAttribute("width"));
    canvas.setAttribute("height", document.getElementsByTagName("svg")[0].getAttribute("height"));
    var svgString = new XMLSerializer().serializeToString(document.getElementsByTagName("svg")[0]);
    var DOMURL = self.URL || self.webkitURL || self;
    var svg = new Blob([svgString], {type: "image/svg+xml;charset=utf-8"});
    var url = DOMURL.createObjectURL(svg);
    const link = document.createElement('a')
  link.href = url
  link.download = 'Circuit'
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
  canvas.style.display = "none";
}