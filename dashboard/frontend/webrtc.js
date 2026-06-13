// ==========================================
// SecureWatch AI
// webrtc.js
// ==========================================

let peerConnection = null;

let remoteAudio = null;

const rtcConfig = {

    iceServers: [

        {

            urls: "stun:stun.l.google.com:19302"

        }

    ]

};

// ------------------------------------------
// Initialize
// ------------------------------------------

window.addEventListener(

    "DOMContentLoaded",

    () => {

        remoteAudio = document.getElementById(

            "liveAudioPlayer"

        );

    }

);

console.log(

    "%c🎤 WebRTC Module Loaded",

    "color:#4CAF50;font-size:14px;font-weight:bold"

);