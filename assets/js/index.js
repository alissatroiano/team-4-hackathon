// Regards to https://codepen.io/SNOOPY_PENG/pen/YzGeQPo for the code accessed 10-Dec-2021

const listener = new THREE.AudioListener();

const audio = new THREE.Audio(listener);

document.querySelector("input").addEventListener("change", uploadAudio, false);

const buttons = document.querySelectorAll(".play");
buttons.forEach((button, index) =>
  button.addEventListener("click", () => loadAudio(index))
);


function loadAudio(i) {
  document.getElementById("overlay").innerHTML =
    '<div class="text-loading">Please Wait...</div>';
  const files = [
    "https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Simon_Panrucker/Happy_Christmas_You_Guys/Simon_Panrucker_-_01_-_Snowflakes_Falling_Down.mp3",
    "https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Dott/This_Christmas/Dott_-_01_-_This_Christmas.mp3",
    "https://files.freemusicarchive.org/storage-freemusicarchive-org/music/ccCommunity/TRG_Banks/TRG_Banks_Christmas_Album/TRG_Banks_-_12_-_No_room_at_the_inn.mp3",
    "https://files.freemusicarchive.org/storage-freemusicarchive-org/music/ccCommunity/Mark_Smeby/En_attendant_Nol/Mark_Smeby_-_07_-_Jingle_Bell_Swing.mp3",
  ];
  const file = files[i];

  const loader = new THREE.AudioLoader();
    loader.load(file, function (buffer) {
      audio.setBuffer(buffer);
      audio.play();
    });
}


function uploadAudio(event) {
  document.getElementById("overlay").innerHTML =
    '<div class="text-loading">Please Wait...</div>';
  const files = event.target.files;
  const reader = new FileReader();

  reader.onload = function (file) {
    var arrayBuffer = file.target.result;

    listener.context.decodeAudioData(arrayBuffer, function (audioBuffer) {
      audio.setBuffer(audioBuffer);
      audio.play();
      //analyser = new THREE.AudioAnalyser(audio, fftSize);
      //init();
    });
  };

  reader.readAsArrayBuffer(files[0]);
}



