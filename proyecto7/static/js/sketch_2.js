let capture;
isVideoPlaying = false;
let recorder;



function toggleRecording(){
  if (recorder.state != 'recording'){
    recorder.start();
  } else {
    // https://stackoverflow.com/a/34259326
    recorder.ondataavailable = e => {
      // video = createVideo(URL.createObjectURL(e.data), videoLoad);
      csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
      blob = e.data;
      var xhttp = new XMLHttpRequest();xhttp.open("POST", "/experimentos/get", true);
      xhttp.setRequestHeader('X-CSRFToken', document.querySelector('[name=csrfmiddlewaretoken]').value);
      var data = new FormData();
      data.append('data', blob, 'RECORD');
      
      data.append('order', orden);
      data.append('uuid', uuid);
      xhttp.send(data);
    };

    recorder.stop();
  }
}

function draw() {
}

function setup() {

  var constraints = {
    video: {
      mandatory: {
        minWidth: 330,
        minHeight: 240,
        echoCancellation: true, // is this working??
      },
      optional: [{ maxFrameRate: 30}],
    },
    audio: false 
  };
  capture = createCapture(constraints, function(stream)   {    
    // create a recorder object with the camera stream
    recorder = new MediaRecorder(stream, {
      // mimeType: 'video/mp4'
    });
  });
}
