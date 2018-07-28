//var d3 = require("d3"),
  //  cloud = require("../");
var width = 1000, height = 750;
var fill = d3.scale.category20();

var options = "";
var name_ext = "_WordOccurence.csv";
var checked = ""
populate();
function getFile(){
  var radios = document.getElementsByName('DataFrom');
  for (var i = 0, length = radios.length; i < length; i++)
  {
   if (radios[i].checked)
   {
    // do whatever you want with the checked radio
    checked = radios[i].value + name_ext;
    // only one radio can be logically checked, don't check the rest
    break;
   }
  }
}
function populate(){
getFile();
document.getElementById("word-cloud").innerHTML = "";
document.getElementById("sel1").innerHTML = "";
d3.csv(checked,function(data){

var words = data
  .map(function(d) {return d.word; });

words = words.filter(function(v,i) { return words.indexOf(v) == i; });
options = ""
for (opt in words) {
    options += "<option>" + words[opt] + "</option>";
  }

document.getElementById("sel1").innerHTML = options;
});
}
var occurence;
function generate_wordcloud(){
  getFile();
  var e = document.getElementById("sel1");
  d3.csv(checked,function(data){
    occurence = data
    .filter(function(d) {return d.word == e.options[e.selectedIndex].text;})
    .map(function(d) {return {text: d.occurrence,size: 24}; })
    .slice(0,100);

    generate();
  });
}
function generate(){
  document.getElementById("word-cloud").innerHTML = "";
d3.layout.cloud()
  .size([width, height])
  .words(occurence)
  .padding(5)
  .rotate(function() { return ~~(Math.random() * 2) * 90; })
  .font("Impact")
  .fontSize(function(d) { return d.size; })
  .on("end", draw)
  .start();
}
function draw(words) {
  d3.select("#word-cloud").append("svg")
      .attr("width", width)
      .attr("height", height)
    .append("g")
      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")")
    .selectAll("text")
      .data(words)
    .enter().append("text")
      .style("font-size", function(d) { return d.size + "px"; })
      .style("font-family", "Impact")
      .style("fill", function(d, i) { return fill(i); })
      .attr("text-anchor", "middle")
      .attr("transform", function(d) {
        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
      })
      .text(function(d) { return d.text; });
}
