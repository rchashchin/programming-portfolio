// ===== Footer year =====
document.getElementById("year").textContent = new Date().getFullYear();

// ===== Mobile navigation =====
const toggle = document.querySelector(".nav-toggle");
const nav = document.getElementById("site-nav");

toggle.addEventListener("click", () => {
  const open = toggle.getAttribute("aria-expanded") === "true";
  toggle.setAttribute("aria-expanded", String(!open));
  nav.classList.toggle("open", !open);
});

// Close the menu after choosing a link
nav.querySelectorAll("a").forEach((link) =>
  link.addEventListener("click", () => {
    toggle.setAttribute("aria-expanded", "false");
    nav.classList.remove("open");
  })
);

// ===== Booking request form =====
const form = document.querySelector(".request-form");
const statusEl = form.querySelector(".form-status");
const submitBtn = form.querySelector('button[type="submit"]');

// Don't allow dates in the past
form.querySelector("#date").min = new Date().toISOString().split("T")[0];

function setStatus(message, type) {
  statusEl.textContent = message;
  statusEl.className = `form-status ${type || ""}`;
}

function validate() {
  let firstInvalid = null;
  form.querySelectorAll("[required]").forEach((input) => {
    const field = input.closest(".field");
    const ok = input.checkValidity();
    field.classList.toggle("invalid", !ok);
    if (!ok && !firstInvalid) firstInvalid = input;
  });
  if (firstInvalid) firstInvalid.focus();
  return !firstInvalid;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  if (!validate()) {
    setStatus("Please fill in the highlighted fields.", "error");
    return;
  }

  submitBtn.disabled = true;
  setStatus("Sending…");

  try {
    const response = await fetch(form.action, {
      method: "POST",
      body: new FormData(form),
      headers: { Accept: "application/json" },
    });

    if (!response.ok) throw new Error(`Request failed: ${response.status}`);

    form.reset();
    setStatus("Thank you! Your request has been sent — Elena will be in touch soon.", "success");
  } catch (error) {
    setStatus("Sorry, something went wrong. Please try again or email directly.", "error");
  } finally {
    submitBtn.disabled = false;
  }
});
