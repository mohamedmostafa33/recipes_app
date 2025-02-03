document.addEventListener("DOMContentLoaded", function () {
    // Confirm before deleting a recipe
    const deleteButtons = document.querySelectorAll(".delete-recipe");
    deleteButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            const confirmDelete = confirm("Are you sure you want to delete this recipe?");
            if (!confirmDelete) {
                event.preventDefault();
            }
        });
    });

    // Highlight the active navigation link
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    navLinks.forEach(link => {
        if (link.href === window.location.href) {
            link.classList.add('active');
        }
    });
});
