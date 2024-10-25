// accordion handler
document.querySelectorAll(".accordion-header").forEach((header) => {
  header.addEventListener("click", function () {
    const content = header.nextElementSibling;
    const isActive = content.classList.contains("active");

    document.querySelectorAll(".accordion-content").forEach((content) => {
      content.classList.remove("active");
      content.previousElementSibling.classList.remove("active");
    });

    if (!isActive) {
      content.classList.add("active");
      header.classList.add("active");
    }
  });
});

// form handler
document
  .getElementById("predictionForm")
  .addEventListener("submit", function (e) {
    const inputs = document.querySelectorAll("input");
    let valid = true;

    inputs.forEach((input) => {
      if (!input.value) {
        valid = false;
      }
    });

    if (!valid) {
      e.preventDefault();
      alert("Mohon lengkapi semua field sebelum submit.");
    }
  });

// Predict button handler
document.getElementById("predictButton").addEventListener("click", function () {
  const formData = new FormData(document.getElementById("predictionForm"));

  fetch("/", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.prediction_text) {
        if (data.prediction_text === "Diabetes") {
          document.getElementById(
            "diabetes-text"
          ).innerHTML = `<span class="green-text">${data.prediction_text}</span>`;
        } else {
          document.getElementById(
            "diabetes-text"
          ).innerHTML = `<span class="red-text">${data.prediction_text}</span>`;
        }

        const resultContainer = document.getElementById("predictionResult");

        // Clear previous results
        resultContainer.innerHTML = "";

        // Display input results
        for (let key in data.input_data) {
          const resultItem = document.createElement("div");
          resultItem.classList.add("result-item"); // Add class for styling
          resultItem.innerHTML = `<span class="key">${key}:</span> <span class="value">${data.input_data[key]}</span>`;
          resultContainer.appendChild(resultItem);
        }

        const classificationReport = `
        <h3>Classification Report:</h3>
        <table>
          <thead>
            <tr>
              <th></th>
              <th>Precision</th>
              <th>Recall</th>
              <th>F1-Score</th>
              <th>Support</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Tidak Diabetes</td>
              <td>0.83</td>
              <td>0.89</td>
              <td>0.86</td>
              <td>100</td>
            </tr>
            <tr>
              <td>Diabetes</td>
              <td>0.77</td>
              <td>0.67</td>
              <td>0.71</td>
              <td>54</td>
            </tr>
            <tr>
              <td colspan="1">Accuracy</td>
              <td></td>
              <td></td>
              <td>0.81</td>
              <td>154</td>
            </tr>
            <tr>
              <td colspan="1">Macro Avg</td>
              <td>0.80</td>
              <td>0.78</td>
              <td>0.79</td>
              <td>154</td>
            </tr>
            <tr>
              <td colspan="1">Weighted Avg</td>
              <td>0.81</td>
              <td>0.81</td>
              <td>0.81</td>
              <td>154</td>
            </tr>
          </tbody>
        </table>
      `;

        resultContainer.innerHTML += classificationReport;
      } else {
        alert("Gagal mendapatkan hasil prediksi.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("Terjadi kesalahan saat melakukan prediksi.");
    });
});

// reload page handler
window.addEventListener("beforeunload", function (event) {
  const confirmationMessage = "Apakah Anda yakin reload halaman ini? ";

  event.returnValue = confirmationMessage;
  return confirmationMessage;
});

// hamburger handler
const hamburger = document.getElementById("hamburger");
const navLinks = document.getElementById("nav-links");

hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("active"); // Toggle class 'active' untuk menampilkan atau menyembunyikan menu
});
