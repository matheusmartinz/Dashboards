const observer = new MutationObserver((mutations, obs) => {
    const inputs = document.querySelectorAll('.dash-filter input');

    if (inputs.length > 0) {
        inputs.forEach(input => {
            input.placeholder = 'Filtrar';
        });
        obs.disconnect(); 
    }
});

observer.observe(document.body, {
    childList: true,
    subtree: true
});
