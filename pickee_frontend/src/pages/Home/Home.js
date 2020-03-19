import Vue from "vue";
import Home from "./Home.vue";

import vuetify from "@/plugins/vuetify/vuetify";
import Responsive from "@/plugins/responsive";

new Responsive();

import "@/assets/styles/app.css";
import "@/assets/styles/pages/home.css";

Vue.config.productionTip = false;

new Vue({
    vuetify,
    render: h => h(Home)
}).$mount("#home");
