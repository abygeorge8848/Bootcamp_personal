var canvas = document.querySelector('canvas');
var scale = 1.5

width = window.innerWidth;
height = window.innerHeight*.96;

canvas.width = width
canvas.height = height

var ctx = canvas.getContext('2d');

lightRayList = []
mirrorList = []
buttonList = []


function addLightRay(){
    lightRayList.push(new lightRay(Math.random() * width * .6 + width * .1, Math.random() * height * .3 + height * .6, -Math.random()*Math.PI*2))
}

function addMirror(){
    mirrorList.push(new mirror(Math.random() * width * .6 + width * .1, Math.random() * height * .8 + height * .1, 0));
}

function addButton(){
    buttonList.push(new button(Math.random() * width * .6 + width * .1, Math.random() * height * .8 + height * .1));
}


function lightRay(x, y, angle){
    this.x = x;
    this.y = y;
    this.angle = angle;

    var xx = this.x + 100000 * Math.cos(this.angle);
    var yy = this.y + 100000 * Math.sin(this.angle);
  
    ctx.strokeStyle = ("rgba(255,255,0,1)");
    ctx.lineWidth=1*scale;
    ctx.beginPath();
    ctx.moveTo(this.x, this.y);
    ctx.lineTo(xx, yy);
    ctx.stroke();
    ctx.closePath();
}

function mirror(x, y, angle){

    this.x = x;
    this.y = y;
    this.angle = angle;

    var xx = this.x + 300 * Math.cos(this.angle);
    var yy = this.y + 300 * Math.sin(this.angle);
  
    ctx.strokeStyle = ("rgba(255,255,0,1)");
    ctx.lineWidth=5*scale;
    ctx.beginPath();
    ctx.moveTo(this.x, this.y);
    ctx.lineTo(xx, yy);
    ctx.stroke();
    ctx.closePath();

}

function button(x, y){
    this.x = x;
    this.y = y;
    
}


document.getElementById("addLightRayButton").addEventListener("click", addLightRay);
document.getElementById("addMirrorButton").addEventListener("click", addMirror);
document.getElementById("Button").addEventListener("mousemove", addButton);

