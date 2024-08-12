document.addEventListener('DOMContentLoaded', function() {
    const keys = document.querySelectorAll('.key');

    function applyJiggle(key) {
        const keyElement = document.querySelector(`.key[data-key="${key}"]`);
        if (keyElement) {
            keyElement.classList.add('jiggle');
            setTimeout(() => keyElement.classList.remove('jiggle'), 500); // 
        }
    }

    async function toggleLogging(enable) {
        try {
            const endpoint = enable ? '/enable-logging' : '/disable-logging';
            await fetch(endpoint, { method: 'POST' });
        } catch (error) {
            console.error('Error toggling keylogging:', error);
        }
    }

    toggleLogging(true);
    window.addEventListener('beforeunload', () => {
        toggleLogging(false);
    });

    setInterval(async function() {
        try {
            const response = await fetch('/check-keypress');
            if (response.ok) {
                const data = await response.json();
                if (data.keyPressed) {
                    applyJiggle(data.keyPressed);
                }
            }
        } catch (error) {
            console.error('Error polling for keypress:', error);
        }
    }, 100); 
});
