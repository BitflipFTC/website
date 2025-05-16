document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('mousemove', (event) => {
        const rect = card.getBoundingClientRect();
        const mouseX = event.clientX - rect.left; // Mouse X within card
        const mouseY = event.clientY - rect.top;  // Mouse Y within card

        let rotateY = ((mouseX / rect.width) - 0.5) * 40; // Left/Right rotation
        let rotateX = ((mouseY / rect.height) - 0.5) * -40; // Up/Down rotation

        rotateX *= 0.6;
        rotateY *= 0.6;

        card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.1)`;
    });

    card.addEventListener('mouseleave', () => {
        card.style.transform = 'rotateX(0deg) rotateY(0deg)'; // Reset on mouse leave
    });
});
