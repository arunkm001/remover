// script.js
document.getElementById('upload').addEventListener('change', async function (e) {
  const files = [...e.target.files];
  for (const file of files) {
    const formData = new FormData();
    formData.append('image', file);
    
    const res = await fetch('/remove-text', {
      method: 'POST',
      body: formData
    });

    const data = await res.json();
    if (data.image_url) {
      const img = document.createElement('img');
      img.src = data.image_url;
      document.getElementById('images').appendChild(img);
    }
  }
});
