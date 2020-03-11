/**
 * TEMPORARY
 * TO BE REMOVED
 */

import Vue from "vue";
import Demo from "./_Demo.vue";

import vuetify from "@/plugins/vuetify/vuetify";

import "@/assets/styles/app.css";

Vue.config.productionTip = false;

new Vue({
    vuetify,
    render: h => h(Demo)
}).$mount("#demo");
