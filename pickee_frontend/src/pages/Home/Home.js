import Vue from "vue";
import Home from "./Home.vue";

import vuetify from "@/plugins/vuetify/vuetify";

import "@/assets/styles/app.css";
// import "@/assets/styles/pages/home.css";

Vue.config.productionTip = false;

new Vue({
    vuetify,
    render: h => h(Home)
}).$mount("#home");
