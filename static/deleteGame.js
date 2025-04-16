document.addEventListener("DOMContentLoaded", function() {
    const deleteForms = document.querySelectorAll('.delete-form');
    deleteForms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            const gameTitle = form.getAttribute('data-title') || "this game";
            const confirmed = confirm(`Are you sure you want to delete "${gameTitle}"?`);
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });

    setTimeout(function() {
        const messages = document.querySelectorAll('.message');
        messages.forEach(function(msg) {
            msg.style.transition = "opacity 0.5s";
            msg.style.opacity = 0;
            setTimeout(function() {
                msg.style.display = "none";
            }, 500);
        });
    }, 3000);
}); 