from socket_manager import socketio


# ----------------------------
# WebRTC Offer
# ----------------------------

@socketio.on("webrtc_offer")
def webrtc_offer(data):

    socketio.emit(

        "webrtc_offer",

        data,

        broadcast=True,

        include_self=False

    )


# ----------------------------
# WebRTC Answer
# ----------------------------

@socketio.on("webrtc_answer")
def webrtc_answer(data):

    socketio.emit(

        "webrtc_answer",

        data,

        broadcast=True,

        include_self=False

    )


# ----------------------------
# ICE Candidate
# ----------------------------

@socketio.on("webrtc_candidate")
def webrtc_candidate(data):

    socketio.emit(

        "webrtc_candidate",

        data,

        broadcast=True,

        include_self=False

    )