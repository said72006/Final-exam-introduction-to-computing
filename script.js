"use strict";
// Educational form preview. It deliberately makes no network request
// and does not persist any submitted information.
const form = document.getElementById("demo-registration-form");
const status = document.getElementById("form-status");
if (form && status) {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    status.textContent = "Demo validated successfully. No data was sent or saved; this is not a real enrollment.";
    form.reset();
  });
}
