const botao = document.querySelector("#botaomostrar");

botao.addEventListener("click", async () => {
  const cidade = document.querySelector("#nomecidade").value;
  const campoinfo = document.querySelector("#infos");

  const resposta = await fetch(`api/clima-local/${cidade}`);

  const climajson = await resposta.json();
  const clima = JSON.parse(climajson);

  const lugar = document.querySelector("#lugar");
  const temperatura = document.querySelector("#temperatura");
  const descricao = document.querySelector("#descricao");
  const vento = document.querySelector("#vento");
  const umidade = document.querySelector("#umidade");
  const chuva = document.querySelector("#chuva");
  const hora = document.querySelector("#hora");
  const icone = document.querySelector("#icone");

  temperatura.innerHTML = clima.temperatura + "°C";
  lugar.innerHTML = clima.local;
  descricao.innerHTML = clima.descricao;
  vento.innerHTML = "Vento: " + clima.vento + "km/h";
  umidade.innerHTML = "Umidade: " + clima.umidade + "%";
  chuva.innerHTML = "Chuva: " + clima.chuva + "%";
  hora.innerHTML = clima.hora;
});

const botaotema = document.querySelector("#mododark");

botaotema.addEventListener("click", tema => {
  document.body.classList.toggle("dark");
});
