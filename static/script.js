document.getElementById('uploadForm').onsubmit = async function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('/process-report', {
        method: 'POST',
        body: formData,
    });
    const result = await response.json();
    document.getElementById('responseMessage').innerText = result.message || result.error;

    if (response.ok) {
        document.getElementById('results').style.display = 'block';
        document.getElementById('analysisResult').innerText = JSON.stringify(result.analysis, null, 2);
        document.getElementById('healthRecommendations').innerText = result.recommendations.join(', ');
        document.getElementById('relatedArticles').innerHTML = result.articles.map(article => `<a href="${article}" target="_blank">${article}</a>`).join('<br>');
    }
};


document.addEventListener("DOMContentLoaded", () => {
    // Smooth scrolling for anchors
    const links = document.querySelectorAll('a[href^="#"]');
    for (let link of links) {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    }

    // Form submission animation
    const form = document.getElementById("uploadForm");
    form.addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent default form submission
        // Show loading animation or message
        const loadingMessage = document.createElement("div");
        loadingMessage.textContent = "Processing...";
        loadingMessage.className = "loading";
        document.body.appendChild(loadingMessage);

        // Simulate a delay for processing (remove this in production)
        setTimeout(() => {
            form.submit(); // Submit the form
        }, 2000); // Adjust delay as needed
    });
});
