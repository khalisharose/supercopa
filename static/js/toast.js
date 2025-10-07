function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toastComponent) return;

    toastComponent.style.backgroundColor = '';
    toastComponent.style.color = '';
    toastComponent.style.border = '';

    // Warna diambil dari palet: 
    // #F8BDBB (pink muda), #DDE255 (kuning kehijauan), #F98805 (oranye), 
    // #F35695 (pink cerah), #264414 (hijau tua)
    if (type === 'success') {
        toastComponent.style.backgroundColor = '#DDE255'; // hijau lemon cerah
        toastComponent.style.color = '#264414';           // hijau tua
        toastComponent.style.border = '2px solid #264414';
    } else if (type === 'error') {
        toastComponent.style.backgroundColor = '#F35695'; // pink cerah
        toastComponent.style.color = '#fff';              
        toastComponent.style.border = '2px solid #F98805'; // oranye tegas
    } else if (type === 'warning') {
        toastComponent.style.backgroundColor = '#F98805'; // oranye
        toastComponent.style.color = '#fff';
        toastComponent.style.border = '2px solid #264414'; // hijau tua
    } else {
        toastComponent.style.backgroundColor = '#F8BDBB'; // pink muda
        toastComponent.style.color = '#264414';           // hijau tua
        toastComponent.style.border = '2px solid #264414';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}
