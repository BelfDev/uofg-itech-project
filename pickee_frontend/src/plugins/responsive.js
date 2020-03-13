'use strict';

import MobileDetect from 'mobile-detect';

const BASE_WIDTH = {
    desktop: 1920,
    tablet: 768,
    phone: 320
};
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
        // If window size is larger than minimal size - change root font size
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
        const targetWidth = this.device === 'phone'
            ? document.documentElement.clientWidth
            : Math.min(this.$window.innerWidth, baseWidth);
        
        console.log(
            this.$window.innerWidth,
            document.documentElement.clientWidth,
            targetWidth
        );
        
        const size = (targetWidth / baseWidth) * BASE_SIZE + 'px';
        
        return size;
        // const targetWidth = this.getTargetWidth();

        // return (targetWidth / BASE_WIDTH) * BASE_SIZE + "px"
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
}