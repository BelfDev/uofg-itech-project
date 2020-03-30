'use strict';

import MobileDetect from 'mobile-detect';

const BASE_WIDTH = {
    desktop: 1920,
    tablet: 768,
    phone: 320
};
const DESKTOP_MIN_WIDTH = 1024;
const BASE_SIZE = 10;

export default class {
    constructor() {
        this.md = new MobileDetect(window.navigator.userAgent);
        this.$html = document.documentElement;
        this.$window = window;
        this.device;

        this.init();
    }

    /**
     * Initialization
     */
    init() {
        this.device = this.detectDevice();
        this.runScreenResize();
        this.bindEvents();
    }

    detectDevice() {
        let device = 'desktop';

        if (this.md.tablet()) {
            device = 'tablet';
        } else if (this.md.mobile()) {
            device = 'phone';
        }

        setTimeout(() => {
            console.log(this.md.os());
            console.log(this.md.userAgent());
            console.log(this._is_touch_device());
            document.body.innerHTML = "OS: " + this.md.os() + "<br />" + "UserAgent: " + this.md.userAgent() + "<br />" + "Is touch: " +  + this._is_touch_device() + "<br />" + "Is mobile: " + this.md.mobile() + "<br />" + "Is tablet: " + this.md.tablet() + "<br />" + "Version: " + this.md.version() + "<br />" + "Is phone: " + this.md.phone();
        }, 5000);

        return device;
    }

    /**
     * Event binding
     */
    bindEvents() {
        this.$window.addEventListener("resize", () => {
            this.switchBodyClasses();
            this.changeBaseFontSize();
        });
    }

    /**
     * Resize screen
     */
    runScreenResize() {
        this.switchBodyClasses();
        this.changeBaseFontSize();
    }

    /**
     * Gets new font size and sets it for root html element
     */
    changeBaseFontSize() {
        const baseWidth = this.calcBaseWidth();
        const size = this.calculateFontSize(baseWidth);
        this.setPageFontSize(size);
    }

    calcBaseWidth() {
        return BASE_WIDTH[this.device];
    }

    /**
     * Gets target width and tweaks font size accordingly
     * @returns {string} Font-size string in px
     */
    calculateFontSize(baseWidth) {
        let targetWidth = document.documentElement.clientWidth;

        if (this.device === 'tablet') {
            targetWidth = Math.min(this.$window.innerWidth, baseWidth);
        } else {
            targetWidth = Math.min(Math.max(this.$window.innerWidth, DESKTOP_MIN_WIDTH), baseWidth);
        }
        
        const size = (targetWidth / baseWidth) * BASE_SIZE + 'px';
        
        return size;
    }

    /**
     * Compares constants and current window width and
     * returns the lowest
     * @returns {number}
     */
    getTargetWidth() {
        return Math.min(this.$window.innerWidth(), BASE_WIDTH)
    }

    /**
     * Sets font size for root html element
     * @param size
     */
    setPageFontSize(size) {
        this.$html.style.fontSize = size;
    }

    switchBodyClasses() {
        const body = document.body;
        const deviceClassNames = ['desktop', 'tablet', 'phone'];

        deviceClassNames.forEach(className => body.classList.remove(className));
        body.classList.add(this.device);
    }

    _is_touch_device() {
        try {  
            document.createEvent("TouchEvent");  
            return true;  
        } catch (e) {  
            return false;  
        }  
    }
}