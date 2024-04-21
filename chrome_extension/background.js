chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
    if (message.action === "sendFormData") {
      fetch('http://0.0.0.0:8000/generate-qr', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(message.data)
      })
      .then(response => response.blob())
      .then(blob => {
        const reader = new FileReader();
        reader.onload = function() {
            const base64Data = reader.result;
            const qrCodeData = base64Data.split(',')[1]; 
            // removing 'data:image/png;base64,' from the base64 data
            chrome.runtime.sendMessage({action: "displayQRCode", qrCodeData: qrCodeData});
        };
        reader.readAsDataURL(blob);
        })
      .catch(error => console.error('Error:', error));
    }
  });
  generateBlobData = () =>{
    return URL.createObjectURL("hii");
  }