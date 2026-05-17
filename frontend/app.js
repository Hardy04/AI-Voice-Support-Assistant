async function uploadAudio() {

    const fileInput = document.getElementById("audioFile");

    const formData = new FormData();

    formData.append("audio", fileInput.files[0]);

    const response = await fetch("http://localhost:8000/voice-query", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    document.getElementById("result").innerText = JSON.stringify(data, null, 2);
}
