'use strict';

/**
 * A class to detect device and adjust the root element's (html) font-size 
 * according to the device width. All the measurements in REM will be
 * based on this font-size
 */

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
        } else if (this._isTouchDevice() && this.md.mobile() == null && this.md.os() == null) {
            device = 'tablet';
        }

        return device;
    }

    bindEvents() {
        this.$window.addEventListener("resize", () => {
            this.switchBodyClasses();
            this.changeBaseFontSize();
        });
    }

    runScreenResize() {
        this.switchBodyClasses();
        this.changeBaseFontSize();
    }

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
     */
    getTargetWidth() {
        return Math.min(this.$window.innerWidth(), BASE_WIDTH)
    }

    setPageFontSize(size) {
        this.$html.style.fontSize = size;
    }

    switchBodyClasses() {
        const body = document.body;
        const deviceClassNames = ['desktop', 'tablet', 'phone'];

        deviceClassNames.forEach(className => body.classList.remove(className));
        body.classList.add(this.device);
    }

    _isTouchDevice() {
        try {  
            document.createEvent("TouchEvent");  
            return true;  
        } catch (e) {  
            return false;  
        }  
    }
}