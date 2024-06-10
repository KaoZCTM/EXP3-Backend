function mostrarAlimentos() {
  let url = "http://localhost:3300/alimentosMascotas";
  fetch(url)
    .then((response) => response.json())
    .then((data) => mostrarAlimentos(data))
    .catch((error) => console.log(error));

  const mostrarAlimentos = (data) => {
    console.log(data);
    let texto = "";
    let especie = document.getElementById("especie").value;
    console.log(especie);
    if (especie == "") {
      for (i = 0; i < data.length; i++) {
        texto += `<tr>
                <td>${data[i].id}</td>
                <td>${data[i].marca}</td>
                <td>${data[i].especie}</td>
                <td>${data[i].edad}</td>
                <td>${data[i].ingredientes}</td>
                </tr>`;
      }
      document.getElementById("alimentosMascotas").innerHTML = texto;
    } else {
      buscarEspecie(especie);
    }
  };
}

function buscarEspecie(especie) {
  let url = "http://localhost:3300/alimentosMascotas";
  fetch(url)
    .then((response) => response.json())
    .then((data) => buscarData(data))
    .catch((error) => console.log(error));

  const buscarData = (data) => {
    console.log(data);
    let texto = "";

    if (document.getElementById("especie").selectedIndex == 0) {
      mostrarAlimentos();
    } else {
      for (i = 0; i < data.length; i++) {
        if (especie == data[i].especie) {
          texto += `<tr>
                <td>${data[i].id}</td>
                <td>${data[i].marca}</td>
                <td>${data[i].especie}</td>
                <td>${data[i].edad}</td>
                <td>${data[i].ingredientes}</td>
                </tr>`;
        }
      } //for
      document.getElementById("alimentosMascotas").innerHTML = texto;
    }
  };
}
