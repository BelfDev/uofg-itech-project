import Navigation from "@/components/Navigation/Navigation.vue";
import HeaderAuth from "@/components/HeaderAuth/HeaderAuth.vue";
import Logo from "@/components/Logo/Logo.vue";

export default {
    name: "PageHeader",
    props: {
        logo: Boolean,
        isAboutPage: Boolean,
        user: Object,
        urls: Object
    },
    components: {
        Navigation, 
        HeaderAuth, 
        Logo
    }
}