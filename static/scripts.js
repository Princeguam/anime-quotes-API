// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    });
  });
});

// Highlight active section in sidebar
const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll("aside a");

window.addEventListener("scroll", () => {
  let current = "";
  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    if (window.pageYOffset >= sectionTop - 100) {
      current = section.getAttribute("id");
    }
  });

  navLinks.forEach((link) => {
    link.classList.remove("bg-gray-100");
    if (link.getAttribute("href").substring(1) === current) {
      link.classList.add("bg-gray-100");
    }
  });
});

// Clipboard functionality
const clipboard = new ClipboardJS(".copy-btn");
const toast = document.getElementById("copyToast");

clipboard.on("success", function (e) {
  toast.style.display = "block";
  setTimeout(() => {
    toast.style.display = "none";
  }, 2000);
  e.clearSelection();
});
