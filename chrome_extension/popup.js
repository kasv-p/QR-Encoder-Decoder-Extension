
document.getElementById('form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = {
      payee_name: document.getElementById('payee_name').value,
      payee_vpa: document.getElementById('payee_vpa').value,
      account_no: document.getElementById('account_no').value,
      ifsc_code: document.getElementById('ifsc_code').value,
      type: document.getElementById('type').value
    };
    chrome.runtime.sendMessage({ action: "sendFormData", data: formData });
  });

  document.getElementById('button').addEventListener('click', function(event) {
    event.preventDefault();
    decodedTextElement = document.getElementById('decoded-text');
    
    var fileInput = document.getElementById('image-input');
    var file = fileInput.files[0];
    
    var formData = new FormData();
    formData.append('image', file);
    
    fetch('http://localhost:8000/decode-qr', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        decodedTextElement.innerHTML = data;
    })
    .catch(error => {
        console.error('Error:', error);
    });
    
  });
  
  chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
    if (message.action === "displayQRCode") {
        console.log(message, "message.data")
        const qrCodeImg = document.getElementById('qrCodeImg');
        qrCodeImg.src = 'data:image/png;base64,' + message.qrCodeData;
    }
  })