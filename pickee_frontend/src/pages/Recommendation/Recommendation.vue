import Vue from "vue";
import App from "./App.vue";

import vuetify from "@/plugins/vuetify/vuetify";

import "@/assets/styles/app.css";
import "@/assets/styles/pages/about.css";

Vue.config.productionTip = false;

new Vue({
    vuetify,
    render: h => h(App)
}).$mount("#about");
