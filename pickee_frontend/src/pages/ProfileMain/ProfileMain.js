import Vue from "vue";
import ProfileMain from "./ProfileMain.vue";

import vuetify from "@/plugins/vuetify/vuetify";
import Responsive from "@/plugins/responsive";

new Responsive();

import "@/assets/styles/app.css";
import "@/assets/styles/pages/profile.css";

Vue.config.productionTip = false;

new Vue({
    vuetify,
    render: h => h(ProfileMain)
}).$mount("#profile-main");
