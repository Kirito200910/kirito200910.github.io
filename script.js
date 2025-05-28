
document.getElementById('dni-form').addEventListener('submit', async function(e) {
  e.preventDefault();

  const form = e.target;
  const data = Object.fromEntries(new FormData(form).entries());

  const canvas = document.getElementById('dniCanvas');
  const ctx = canvas.getContext('2d');

  const img = new Image();
  img.src = 'dni_plantilla.png';
  img.onload = () => {
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
    ctx.font = "16px Arial";
    ctx.fillStyle = "black";

    ctx.fillText(`Nombre: ${data.nombre}`, 50, 100);
    ctx.fillText(`Sexo: ${data.sexo}`, 50, 130);
    ctx.fillText(`Nacionalidad: ${data.nacionalidad}`, 50, 160);
    ctx.fillText(`Nacimiento: ${data.fechaNacimiento}`, 50, 190);
    ctx.fillText(`Lugar: ${data.lugarNacimiento}`, 50, 220);
    ctx.fillText(`DNI: ${data.numeroDNI}`, 50, 250);
    ctx.fillText(`Autenticidad: ${data.tecnica}`, 50, 280);
    ctx.fillText(`Caducidad: ${data.caducidad}`, 50, 310);
    ctx.fillText(`Info extra: ${data.infoExtra}`, 50, 340);
  };

  try {
    await fetch('https://script.google.com/macros/s/TU_SCRIPT_ID/exec', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: { 'Content-Type': 'application/json' },
    });

    window.open("bienvenida.html", "_blank");
  } catch (err) {
    alert("Error al enviar datos.");
    console.error(err);
  }
});
