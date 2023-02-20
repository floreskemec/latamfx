// Make a request to the backend to get a list of currencies
fetch("http://localhost:8000/currencies")
  .then(response => response.json())
  .then(data => {
    const select = document.getElementById("currency-select");
    // Add each currency to the dropdown menu
    for (let i = 0; i < data.length; i++) {
      const option = document.createElement("option");
      option.text = `${data[i].name} (${data[i].code})`;
      option.value = data[i].code;
      select.add(option);
    }
  })
  .catch(error => console.error(error));

// Make a request to the backend when the form is submitted
const form = document.getElementById("investment-form");
form.addEventListener("submit", event => {
  event.preventDefault();
  const formData = new FormData(event.target);
  const amount = formData.get("amount");
  const date = formData.get("date");
  const currency = formData.get("currency");
  // Make a request to the backend to get the best investment
  fetch(`http://localhost:8000/best-investment?amount=${amount}&date=${date}&currency=${currency}`)
    .then(response => response.json())
    .then(data => {
      // Display the results on the page
      const resultDiv = document.getElementById("result");
      resultDiv.innerHTML = `
        <h2>Best Investment</h2>
        <p>You should buy ${data.amount_invested.toFixed(2)} worth of ${currency} to get a profit of ${data.profit.toFixed(2)} (${data.percentage_profit.toFixed(2)}%).</p>
        <p>The best currencies to invest in are ${data.currencies.join(", ")}</p>
      `;
    })
    .catch(error => console.error(error));
});
