$(function () {
  $("#formularioRegistro").validate({
    rules: {
      nom: {
        required: true,
      },

      ape: {
        required: true,
      },

      correo: {
        required: true,
        email: true,
      },

      telefono: {
        required: false,
        number: true,
      },

      fecha: {
        required: true,
      },

      pass1: {
        required: true,
      },

      pass2: {
        required: true,
        equalTo: "#pass1",
      },
    },

    messages: {
      nom: {
        required: "Ingrese su nombre.",
        minlength: "Caracteres insuficientes, debe tener al menos 3 letras.",
      },

      ape: {
        required: "Ingrese su nombre.",
        minlength: "Caracteres insuficientes, debe tener al menos 3 letras.",
      },

      correo: {
        required: "Ingrese su correo electrónico",
        email: "Formato de correo inválido",
      },

      telefono: {
        required: "Ingrese su número de teléfono",
        number: "Teléfono inválido.",
        minlength: "Digitos insuficientes.",
        maxlength: "Teléfono inválido.",
      },

      fecha: {
        required: "Seleccione su fecha..",
        min: "Fecha de ingreso no válida..",
      },

      pass1: {
        required: "Ingrese su contraseña..",
        minlength: "Carácteres insuficientes",
      },

      pass2: {
        required: "Reingrese su contraseña..",
        minlength: "Carácteres insuficientes",
        equalTo: "Contraseñas no coinciden",
      },
    },
  });
});
