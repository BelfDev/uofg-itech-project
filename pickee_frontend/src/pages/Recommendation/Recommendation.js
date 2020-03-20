import Vue from "vue";
import axios from 'axios';
import VueAxios from 'vue-axios';
import Recommendation from "./Recommendation.vue";

import vuetify from "@/plugins/vuetify/vuetify";
import Responsive from "@/plugins/responsive";

new Responsive(); 
Vue.use(VueAxios, axios);

import "@/assets/styles/app.css";
import "@/assets/styles/pages/recommendation.css";

Vue.config.productionTip = false;

new Vue({
    vuetify,
    render: h => h(Recommendation)
}).$mount("#recommendation");
