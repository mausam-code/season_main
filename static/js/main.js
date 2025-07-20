class ClockSystem {
    constructor() {
        this.digitalTimeElement = document.getElementById('digitalTime');
        this.digitalDateElement = document.getElementById('digitalDate');
        this.timezoneElement = document.getElementById('timezone');
        this.hourHand = document.getElementById('hourHand');
        this.minuteHand = document.getElementById('minuteHand');
        this.secondHand = document.getElementById('secondHand');
        
        this.init();
    }
    
    init() {
        this.updateClock();
        setInterval(() => this.updateClock(), 1000);
        this.setTimezone();
    }
    
    updateClock() {
        const now = new Date();
        this.updateDigitalClock(now);
        this.updateAnalogClock(now);
    }
    
    updateDigitalClock(now) {
        // Digital time
        const timeString = now.toLocaleTimeString('en-US', {
            hour12: false,
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        });
        
        // Date
        const dateString = now.toLocaleDateString('en-US', {
            weekday: 'short',
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });
        
        if (this.digitalTimeElement) {
            this.digitalTimeElement.textContent = timeString;
        }
        
        if (this.digitalDateElement) {
            this.digitalDateElement.textContent = dateString;
        }
    }
    
    updateAnalogClock(now) {
        const hours = now.getHours() % 12;
        const minutes = now.getMinutes();
        const seconds = now.getSeconds();
        
        // Calculate angles
        const secondAngle = (seconds * 6); // 360/60 = 6 degrees per second
        const minuteAngle = (minutes * 6) + (seconds * 0.1); // 360/60 = 6 degrees per minute
        const hourAngle = (hours * 30) + (minutes * 0.5); // 360/12 = 30 degrees per hour
        
        // Apply rotations
        if (this.secondHand) {
            this.secondHand.style.transform = `rotate(${secondAngle}deg)`;
        }
        
        if (this.minuteHand) {
            this.minuteHand.style.transform = `rotate(${minuteAngle}deg)`;
        }
        
        if (this.hourHand) {
            this.hourHand.style.transform = `rotate(${hourAngle}deg)`;
        }
    }
    
    setTimezone() {
        const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
        const offset = new Date().getTimezoneOffset();
        const offsetHours = Math.floor(Math.abs(offset) / 60);
        const offsetMinutes = Math.abs(offset) % 60;
        const sign = offset > 0 ? '-' : '+';
        
        const timezoneString = `${timezone} (UTC${sign}${offsetHours.toString().padStart(2, '0')}:${offsetMinutes.toString().padStart(2, '0')})`;
        
        if (this.timezoneElement) {
            this.timezoneElement.textContent = timezoneString;
        }
    }
}

// Initialize clock when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ClockSystem();
    initializeInteractivity();
});

function initializeInteractivity() {
    // Add hover effects to project cards
    document.querySelectorAll('.project-card').forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Open preview modal
    document.querySelectorAll('.btn-primary').forEach(btn => {
        btn.addEventListener('click', e => {
            e.preventDefault();
            const url = btn.getAttribute('href');
            const modal = document.getElementById('previewModal');
            const content = document.getElementById('previewContent');
            
            if (modal && content) {
                content.innerHTML = `<iframe src="${url}" style="width:100%;height:70vh;border:none;"></iframe>`;
                modal.style.display = 'flex';
            }
        });
    });

    // Close preview modal
    const closeBtn = document.getElementById('closePreview');
    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            const modal = document.getElementById('previewModal');
            if (modal) {
                modal.style.display = 'none';
            }
        });
    }

    // Add ripple effect to buttons
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('click', e => {
            // Create ripple effect
            const ripple = document.createElement('span');
            const rect = btn.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size}px;
                left: ${x}px;
                top: ${y}px;
                background: rgba(255, 255, 255, 0.3);
                border-radius: 50%;
                transform: scale(0);
                animation: ripple 0.6s linear;
                pointer-events: none;
            `;
            
            btn.appendChild(ripple);
            
            setTimeout(() => {
                if (ripple.parentNode) {
                    ripple.remove();
                }
            }, 600);
        });
    });

    // Add ripple keyframes dynamically if not already added
    if (!document.querySelector('#ripple-keyframes')) {
        const style = document.createElement('style');
        style.id = 'ripple-keyframes';
        style.textContent = `
            @keyframes ripple {
                to {
                    transform: scale(2);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
}

// Close modal when clicking outside of it
document.addEventListener('click', (e) => {
    const modal = document.getElementById('previewModal');
    if (modal && e.target === modal) {
        modal.style.display = 'none';
    }
});

// Handle escape key to close modal
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        const modal = document.getElementById('previewModal');
        if (modal && modal.style.display === 'flex') {
            modal.style.display = 'none';
        }
    }
});