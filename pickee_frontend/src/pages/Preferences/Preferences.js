import Vue from "vue";
import Preferences from "./Preferences.vue";

import vuetify from "@/plugins/vuetify/vuetify";
import Responsive from "@/plugins/responsive";

new Responsive();

import "@/assets/styles/app.css";
import "@/assets/styles/pages/profile.css";

Vue.config.productionTip = false;

new Vue({
    vuetify,
    render: h => h(Preferences)
}).$mount("#preferences");
