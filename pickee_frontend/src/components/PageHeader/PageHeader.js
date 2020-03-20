import Navigation from "@/components/Navigation/Navigation.vue";
import HeaderAuth from "@/components/HeaderAuth/HeaderAuth.vue";
import Logo from "@/components/Logo/Logo.vue";

export default {
    name: "PageHeader",
    props: {
        logo: Boolean,
        user: Object
    },
    components: {
        Navigation, 
        HeaderAuth, 
        Logo
    }
}