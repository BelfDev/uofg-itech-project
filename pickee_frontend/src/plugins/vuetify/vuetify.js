/**
 * Vuetify global settings
 */

import Vue from "vue";
import Vuetify from "vuetify/lib";
import customTheme from "./theme";

Vue.use(Vuetify);

const opts = {
    theme: {
        themes: { dark: customTheme },
        dark: true,
        options: {
            customProperties: true
        }
    },
    icons: {
        iconfont: "mdiSvg"
    }
};

export default new Vuetify(opts);
