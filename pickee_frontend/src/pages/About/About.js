import Vue from "vue";
import About from "./About.vue";

import vuetify from "@/plugins/vuetify/vuetify";
import Responsive from "@/plugins/responsive";

new Responsive();

import "@/assets/styles/app.css";
import "@/assets/styles/pages/about.css";

Vue.config.productionTip = false;

new Vue({
    vuetify,
    render: h => h(About)
}).$mount("#about");
