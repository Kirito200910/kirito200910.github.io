function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);

    const ss = SpreadsheetApp.openById("1mf9wqHZV8kNajYOvuEIZ-IIGFN0WluZukTfZNIzmWfk");
    const sheet = ss.getSheetByName("DNI") || ss.insertSheet("DNI");

    sheet.appendRow([
      new Date().toLocaleString(),
      data.nombre,
      data.sexo,
      data.nacionalidad,
      data.fechaNacimiento,
      data.lugarNacimiento,
      data.numeroDNI,
      data.tecnica,
      data.caducidad,
      data.infoExtra
    ]);

    return ContentService.createTextOutput("OK");
  } catch (error) {
    return ContentService.createTextOutput("ERROR: " + error.message);
  }
}
