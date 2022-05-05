// get elements
const canvas = document.getElementById("drawing_canvas")
// get canvas 2d context
const ctx = canvas.getContext('2d');
ctx.fillStyle = "white";
ctx.fillRect(0, 0, canvas.width, canvas.height);

const clear = document.getElementById("clear");
const predict = document.getElementById("predict");
const test = document.getElementById("test_button");

// values
let predicted_val = ""
let predicted_acc = ""
let val_div = document.getElementById("predicted_val")
let acc_div = document.getElementById("predicted_acc")


const canvasOffsetX = canvas.offsetLeft;
const canvasOffsetY = canvas.offsetTop;
let isPainting = false;
let lineWidth = 15;
let startX;
let startY;

// clear canvas
clear.addEventListener("click", (e) => {
    console.log("clear");
    // ctx.clearRect(0, 0, canvas.width, canvas.height);
    // ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  }
);

// get image data from canvas
predict.addEventListener("click", canvasToImage);

// image conversion function
function canvasToImage() {
  let imgData = ctx.getImageData(canvasOffsetX, canvasOffsetY, canvasOffsetX + canvas.width, canvasOffsetY + canvas.height);
  console.log("type: " + typeof(imgData));
  console.log(imgData);
  let dataURL = canvas.toDataURL();
  // console.log(dataURL);
  $.ajax({
    type: 'POST',
    url: '/img',
    data: {
      imageBase64: dataURL
    },
    success: function(data){
      predicted_val = JSON.parse(data.predicted_value);
      predicted_acc = JSON.parse(data.prediction_accuracy);
      val_div.innerHTML = predicted_val
      acc_div.innerHTML = predicted_acc
    },
    error: function(){
      console.log("error!");
    }
  });
}

test.addEventListener("click", e => {
  console.log("test button clicked");
  $.ajax({
    type: 'POST',
    url: '/test',
    data: {"name" : "test"},
    success: function(data){
      console.log(data);
    }
  });
});



// drawing actions
const draw = (e) => {
  if(!isPainting) {
      return;
  }

  ctx.lineWidth = lineWidth;
  ctx.lineCap = 'round';

  ctx.lineTo(e.clientX - canvasOffsetX, e.clientY);
  ctx.stroke();
  
}

canvas.addEventListener('mousedown', (e) => {
  isPainting = true;
  startX = e.clientX;
  startY = e.clientY;
});

canvas.addEventListener('mouseup', e => {
  isPainting = false;
  ctx.stroke();
  ctx.beginPath();
});

canvas.addEventListener('mousemove', draw);

// credits for drawing code: https://www.youtube.com/watch?v=mRDo-QXVUv8